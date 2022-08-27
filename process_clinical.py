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
import shutil
from tqdm import tqdm
pd_file = r"D:\ProjectData\ESDClinical\case_A_combined.csv"
dst_dir = r"D:\ProcessedData\RawVideo1FPS\Bed1\Case A"
src_dir = r"D:\ProcessedData\RawVideo1FPS\Bed1\Cases"
log_data = pd.read_csv(pd_file)
pd_data = log_data.sort_values(by=["Time"])
pd_data["Time"] = pd_data["Time"].apply(lambda x: x.split(".")[0].split("-")[-1])
pd_data = pd_data.drop_duplicates(subset="Time", keep="first")
timestamps = pd_data["Time"].tolist()

annotations = pd_data["Correction"].tolist()
preds = pd_data["Prediction"].tolist()
for idx, annotation in enumerate(annotations):
    if annotation == "--":
        annotations[idx] = preds[idx]

pd_data["Annotation"] = annotations

pd_data = pd_data.drop(labels=["Frame", "Trainer", "FPS","Correction", "Combine"], axis=1)
pd_data.to_csv(os.path.join(dst_dir + ".csv"), index=False)

for timestamp in tqdm(timestamps):
    timestamp = timestamp.replace(":", "_")
    src_file = os.path.join(src_dir, "frame-{}.png".format(timestamp))
    dst_file = os.path.join(dst_dir, os.path.basename(src_file))
    shutil.copy(src_file, dst_file)