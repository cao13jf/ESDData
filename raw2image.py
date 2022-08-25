"""
Sampling from the raw video at 2 FPS for annotating sub dissection
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
from moviepy.video.fx import all
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
    crop_size = args["crop_size"]


    print("Begin {}".format(video_dir))
    save_dir = os.path.join(r"D:\ProcessedData\Vessel_Frames", os.path.basename(video_dir) + "_clipped")
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

    # Crop all frame
    target_video = all.crop(target_video, x1=crop_size[0], y1=crop_size[1], x2=crop_size[2], y2=crop_size[3])
    target_video.write_images_sequence(nameformat=os.path.join(save_dir, "frame-%05d.png"), fps=2, logger=None)

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
    # # video_dirs = ["/Users/jeff/Downloads/27_UH9685651_20150916"]  # "21_E1773023_20131128", "24_M1268525_20131217"
    data_names = ['32_A178_12_9_2017', '33_A178_17_10_2017', '34_A188_25_07_2018', '35_A198_04_01_2019', '36_A198_20_02_2019',
                   '37_A199_18_5_2019', '38_A199_21_6_2019', '40_A167_4_7_2016', '41_A970_17_6_2016', '42_G316314', '44_B384_30_10_2008',
                  '45_C149_23_10_2008', '46_C380_03_07_2008', '47_C380_18_09_2008', '48_D120_17_07_2008', '49_E020_12_02_2009', '50_E119_23_12_2008']
    # data_names = ["35_A198_04_01_2019"]
    label_files = [r"D:\ProjectData\ESDDataPhases\{}.txt".format(x) for x in data_names]
    video_dirs = [r"D:\ProjectData\ESDDataVideos\{}".format(x) for x in data_names]
    crop_sizes = [[175, 70, 690, 530],
                    [178, 48, 690, 530],
                    [85, 20, 337, 222],
                    [175, 50, 590, 530],
                    [175, 50, 690, 530],
                    [175, 50, 690, 530],
                    [175, 50, 690, 530],
                    [175, 50, 690, 530],
                    [175, 50, 690, 530],
                    [175, 50, 690, 530],
                    [170, 40, 683, 520],
                    [170, 40, 683, 520],
                    [170, 40, 683, 520],
                    [170, 40, 683, 520],
                    [170, 40, 683, 520],
                    [170, 40, 683, 520],
                    [170, 40, 683, 520]]

    mpPool = mp.Pool(len(data_names))
    configs = []
    for idx, label_file in enumerate(label_files):
        config = {}
        config['label_file'] = label_file
        config['video_dir'] = video_dirs[idx]
        config["target_phase"] = target_phase
        config["crop_size"] = [175, 50, 690, 530] #crop_sizes[idx]
        configs.append(config.copy())
        # extract_frames(config)
    mpPool.map(extract_frames, configs)
    mpPool.close()
    mpPool.join()