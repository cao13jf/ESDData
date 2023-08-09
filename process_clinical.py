import os
import datetime
from glob import glob
import multiprocessing as mp

import pandas as pd

from video2image import downsample2image

# Rename as time

# date_start = ['23/08/2022-13:03:47.0', '23/08/2022-13:48:07.0', '23/08/2022-14:32:29.0', '23/08/2022-15:16:56.0', '23/08/2022-16:01:18.0', '23/08/2022-16:45:42.0']
# save_dir = r"D:\ProcessedData\RawVideo1FPS\Bed1"
# # date_start = ['23/08/2022-13:01:10.0', '23/08/2022-13:55:55.0', '23/08/2022-14:50:48.0', '23/08/2022-15:45:55.0', '23/08/2022-16:40:39.0', '23/08/2022-17:35:41.0']
# # save_dir = r"D:\ProcessedData\RawVideo1FPS\Bed2"
# video_files = sorted(glob(r"D:\ProjectData\ESDClinical\Bed_2\*"))
# configs = []
# for idx, video_file in enumerate(video_files):
#     img_files = glob(os.path.join(save_dir, "Case {}".format(idx+1), "*.png"))
#     start_time = date_start[idx].split("-")[-1]
#     for idx, img_file in enumerate(img_files):
#         base_name_str = os.path.basename(img_file).split("-")[-1].split(".")[0]
#         date = datetime.datetime.strptime("25/05/01 {}".format(start_time), "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=1000*idx)
#         base_name_time = date.strftime('%H:%M:%S.%f')[:-7]
#         base_name_time = base_name_time.replace(":", "_")
#         target_img_file = os.path.join(os.path.dirname(img_file), os.path.basename(img_file).replace(base_name_str, base_name_time))
#         os.rename(img_file, target_img_file)

# import os
# import pandas as pd
#
# log_file = r"D:\ProjectData\ESDClinical\case_A_combined.csv"
# pd_data = pd.read_csv(log_file)
# pd_data = pd_data.sort_values(by=["Time"])
# pd_data["Time"] = pd_data["Time"].apply(lambda x: x.split(".")[0].split("-")[-1])
# pd_data = pd_data.drop_duplicates(subset="Time", keep="first")



# save_dir = r"D:\ProcessedData\RawVideo1FPS\Bed1"
# # date_start = ['23/08/2022-13:01:10.0', '23/08/2022-13:55:55.0', '23/08/2022-14:50:48.0', '23/08/2022-15:45:55.0', '23/08/2022-16:40:39.0', '23/08/2022-17:35:41.0']
# # save_dir = r"D:\ProcessedData\RawVideo1FPS\Bed2"
# video_files = ["D:\ProcessedData\RawVideo1FPS\Tem\Case 5"]
# configs = []
# for idx, video_file in enumerate(video_files):
#     img_files = glob(os.path.join(video_file,  "*.png"))
#     for idx, img_file in enumerate(img_files):
#         start_time = os.path.basename(img_file).split(".")[0].split("-")[-1].replace("_", ":") + ".0"
#         base_name_str = os.path.basename(img_file).split("-")[-1].split(".")[0]
#         date = datetime.datetime.strptime("25/05/01 {}".format(start_time), "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=1000)
#         base_name_time = date.strftime('%H:%M:%S.%f')[:-7]
#         base_name_time = base_name_time.replace(":", "_")
#         target_img_file = os.path.join(save_dir, os.path.basename(video_file), os.path.basename(img_file).replace(base_name_str, base_name_time))
#         os.rename(img_file, target_img_file)


# Downsample
# downsample2image({"video_file": r"D:\ProjectData\ESDClinical\Bed_1\M_08232022130311_000000000822 yip_1_001_002-1.MP4",
#                   "target_fps": 1,
#                   "start_time": "13:48:06.0",
#                   "save_dir": r"D:\ProcessedData\RawVideo1FPS\Bed1\Case 2"})


# # Collect all images
# import shutil
# from tqdm import tqdm
# pd_file = r"D:\ProjectData\ESDClinical\case_A_combined.csv"
# dst_dir = r"D:\ProcessedData\RawVideo1FPS\Bed1\Case A"
# src_dir = r"D:\ProcessedData\RawVideo1FPS\Bed1\Cases"
# log_data = pd.read_csv(pd_file)
# pd_data = log_data.sort_values(by=["Time"])
# pd_data["Time"] = pd_data["Time"].apply(lambda x: x.split(".")[0].split("-")[-1])
# pd_data = pd_data.drop_duplicates(subset="Time", keep="first")
# timestamps = pd_data["Time"].tolist()
#
# annotations = pd_data["Correction"].tolist()
# preds = pd_data["Prediction"].tolist()
# for idx, annotation in enumerate(annotations):
#     if annotation == "--":
#         annotations[idx] = preds[idx]
#
# pd_data["Annotation"] = annotations
#
# pd_data = pd_data.drop(labels=["Frame", "Trainer", "FPS","Correction", "Combine"], axis=1)
# pd_data.to_csv(os.path.join(dst_dir + ".csv"), index=False)
#
# for timestamp in tqdm(timestamps):
#     timestamp = timestamp.replace(":", "_")
#     src_file = os.path.join(src_dir, "frame-{}.png".format(timestamp))
#     dst_file = os.path.join(dst_dir, os.path.basename(src_file))
#     shutil.copy(src_file, dst_file)

# # Downsample videos to images
# from moviepy.editor import VideoFileClip, concatenate_videoclips
# videos = sorted(glob("/media/jeffery/MedData/ESD/2022_10_18_animal_test/10182022110729_0000000000ai esd/MOVIE/TITLE 001/*.MP4"))
# surgerys = []
# for video in videos:
#     surgerys.append(VideoFileClip(video, audio=False))
#
# surgerys = concatenate_videoclips(surgerys)
# surgerys = surgerys.resize(0.5)
# surgerys.write_videofile("/media/jeffery/MedData/ESD/2022_10_18_animal_test/10182022110729_0000000000ai.MP4", audio=False)


# # Save video clips at different clips
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import all

if __name__ == "__main__":

    bed = "Bed2"
    surgery_start = "11:07:16"
    videos = sorted(glob("/media/jeffery/MedData/ESD/2022_08_23_clinical_test/ex vivo trainee ESD/13.08.2022 1 HK dollar template pig colon/MOVIE/TITLE 001/*.MP4"))
    save_root_dir = "/media/jeffery/MedData/ESD/2022_08_23_clinical_test/ex vivo trainee ESD/Downsampled"
    time_slots = [["11:07:16", "14:06:22"],
                  ["14:06:22", "15:36:43"]]
                  # ["13:24:40", "14:00:00"],
                  # ["14:05:00", "14:21:00"],
                  # ["14:24:00", "14:45:10"],
                  # ["14:56:00", "15:13:20"],
                  # ["15:15:10", "15:50:20"],
                  # ["15:53:20", "16:31:00"]]
    #
    # bed = "Bed1"
    # surgery_start = "11:33:48"
    # videos = sorted(glob("/media/jeffery/MedData/ESD/2022_10_18_animal_test/10182022110729_0000000000ai esd/MOVIE/TITLE 001/*.MP4"))
    # save_root_dir = "/media/jeffery/MedData/ESD/2022_10_18_animal_test/CaseFrames"
    # time_slots = [["12:15:00", "13:43:00"],
    #               ["14:02:00", "14:51:00"],
    #               ["14:56:00", "15:57:00"],
    #               ["16:23:00", "16:54:00"],
    #               ["16:59:00", "17:22:00"]]

    surgerys = []
    for video in videos:
        surgerys.append(VideoFileClip(video, audio=False))

    surgerys = concatenate_videoclips(surgerys)
    # surgerys = all.crop(surgerys, x1=456, y1=0, x2=1800, y2=1080)
    surgerys = surgerys.resize(0.4)
    for idx, time_slot in enumerate(time_slots, start=1):
        save_dir = os.path.join(save_root_dir, bed, "case{}".format(str(idx).zfill(2)))
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        time_start = datetime.datetime.strptime(time_slot[0], "%H:%M:%S") - datetime.datetime.strptime(surgery_start, "%H:%M:%S")
        time_start = "{}.00".format(str(time_start))
        time_end = datetime.datetime.strptime(time_slot[1], "%H:%M:%S") - datetime.datetime.strptime(surgery_start, "%H:%M:%S")
        time_end = "{}.00".format(str(time_end))
        surgery = surgerys.subclip(t_start=time_start, t_end=time_end)
        save_file = "{}/{}_case{}.MP4".format(save_root_dir, bed, str(idx).zfill(2))
        surgery.write_videofile(save_file, audio=False)
        surgery.write_images_sequence(nameformat=os.path.join(save_dir, "%05d.png"), fps=1)

        img_files = sorted(glob(os.path.join(save_dir, "*")), key=lambda x: int(os.path.basename(x).split(".")[0]))
        for img_idx, img_file in enumerate(img_files):
            base_name_str = os.path.basename(img_file).split(".")[0]
            date = datetime.datetime.strptime("25/05/01 {}".format("0:0:0.0"),
                                              "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=1000 * img_idx)
            base_name_str = "{}.png".format(date.strftime('%H:%M:%S.%f')[:-7])
            base_name_str = base_name_str.replace(":", "-")
            target_img_file = os.path.join(save_dir, base_name_str)
            os.rename(img_file, target_img_file)
        print("Finished saving {}".format(save_dir))