"""
Process labelled data by Yueyao
"""
import os
import math
import shutil
import numpy as np
from glob import glob
from tqdm import tqdm

# # Combien multiple videos
import os
import pandas as pd
from glob import glob
from moviepy import editor
import datetime
import multiprocessing as mp
import shutil

def get_stime_stamp(ms):
    us = int(ms)
    date = datetime.datetime.strptime("25/05/01 00:0:0.0", "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=us)  # .strftime('%H:%M:%S.%f')[:-4]
    return date.strftime('%H:%M:%S.%f')[:-4]

def find_clips(frame_idxs, one_frame_duration):
    clip_durations = []  # [[start1, end1], ...]
    gaps = [right - left for left, right in zip(frame_idxs[:-1], frame_idxs[1:])]

    duration = [frame_idxs[0]]
    for idx, gap in enumerate(gaps):
        if gap > 1:
            duration.append(frame_idxs[idx])
            time_strs = [get_stime_stamp(x * one_frame_duration) for x in duration]
            clip_durations.append(time_strs)
            duration = [frame_idxs[idx + 1]]
    duration.append(frame_idxs[-1])
    time_strs = [get_stime_stamp(x * one_frame_duration) for x in duration]
    clip_durations.append(time_strs)

    return clip_durations

def extract_frames(args):
    video_dir = args["video_dir"]
    label_file = args["label_file"]
    target_phase = args["target_phase"]

    print("Begin {}".format(video_dir))
    save_dir = os.path.join(r"E:\ESD\ESD_Vessel_Frames", os.path.basename(video_dir) + "_clipped")
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
        # # Reading videos
    video_files = sorted(glob(os.path.join(video_dir, "*")), key=lambda x: int(x.split("_")[-1].split(".")[0]))  # Collect all video files
    clips = []
    for video_file in video_files:
        clip = editor.VideoFileClip(video_file, audio=False)
        clips.append(clip)
    whole_video = editor.concatenate_videoclips(clips)
    total_frames = int(whole_video.fps * whole_video.duration)
    one_frame_duration = whole_video.fps * 1 / whole_video.fps * 1000  # ms  < default 1 FPS

    # # Reading labels
    phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
    target_phase_frames = phase_label.loc[phase_label["Phase"] == target_phase]
    frame_idxs = target_phase_frames["Frame"].tolist()
    all_durations = find_clips(frame_idxs, one_frame_duration)

    # # get target clips
    target_clips = []
    for all_duration in all_durations:
        one_target_clip = whole_video.subclip(t_start=all_duration[0], t_end=all_duration[1])
        target_clips.append(one_target_clip)
    target_video = editor.concatenate_videoclips(target_clips)
    save_file = os.path.join(save_dir, os.path.basename(video_dir) + ".MP4")
    target_video.write_videofile(save_file, audio=False, codec='mpeg4')
    print("Saving video to {}".format(save_file))

    # # save downsample image
    target_video.write_images_sequence(nameformat=os.path.join(save_dir, "frame-%05d.png"), fps=2)

    img_files = sorted(glob(os.path.join(save_dir, "frame-*.png")))
    for idx, img_file in enumerate(img_files):
        base_name_str = os.path.basename(img_file).split("-")[-1].split(".")[0]
        date = datetime.datetime.strptime("25/05/01 00:0:0.0", "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=500*idx)
        base_name_time = date.strftime('%H:%M:%S.%f')[:-4]
        base_name_time = base_name_time.replace(":", "_").replace(".00", "-1")
        base_name_time = base_name_time.replace(":", "_").replace(".50", "-2")
        target_img_file = os.path.join(save_dir, os.path.basename(img_file).replace(base_name_str, base_name_time))
        os.rename(img_file, target_img_file)
    print("Finished processing {}".format(save_dir))

if __name__ == "__main__":
    target_phase = "sub_dissection"

    # label_files = ["/Users/jeff/Downloads/27_UH9685651.txt"]
    # video_dirs = ["/Users/jeff/Downloads/27_UH9685651_20150916"]  # "21_E1773023_20131128", "24_M1268525_20131217"
    data_names = ["15_A97001983"]
    label_files = [r"E:\ESD\ESD_data_all\phase\{}.txt".format(x) for x in data_names]
    video_dirs = [r"E:\ESD\ESD_data_all\video\{}".format(x) for x in data_names]

    # mpPool = mp.Pool(4)
    configs = []
    for label_file, video_dir in zip(label_files, video_dirs):
        config = {}
        config['label_file'] = label_file
        config['video_dir'] = video_dir
        config["target_phase"] = target_phase
        configs.append(config.copy())
        extract_frames(config)
    # mpPool.map(extract_frames, configs)
    # mpPool.close()
    # mpPool.join()