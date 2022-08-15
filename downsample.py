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

def extract_frames(video_dir):

    print("Begin {}".format(video_dir))
    save_dir = os.path.join(r"F:\ESD\ESD_Vessel_Frames", os.path.basename(video_dir) + "_clipped")
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

        # # Reading videos
    video_files = sorted(glob(os.path.join(video_dir, "*.mpg")))  # Collect all video files
    clip = editor.VideoFileClip(video_files[0], audio=False)

    # # save downsample image
    clip.write_images_sequence(nameformat=os.path.join(save_dir, "frame-%05d.png"), fps=2, logger=None)

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
    data_names = ["08_A17802817", "09_A17813565", ]
    video_dirs = [r"E:\ESD\ESD_data_all\video\{}".format(x) for x in data_names]
    # extract_frames(video_dirs[1])
    mpPool = mp.Pool(2)
    mpPool.map(extract_frames, video_dirs)
    mpPool.close()
    mpPool.join()
