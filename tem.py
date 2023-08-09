# <<<<<<< HEAD
import os
import shutil
import warnings

import pandas as pd

warnings.filterwarnings("ignore")
from tqdm import tqdm
from glob import glob
import moviepy.editor as moviepy

# video_names = ["15_A97001983"]
# video_dirs = [os.path.join(r"E:\ESD\ESD_data_all\video", x) for x in video_names]
# for video_dir in video_dirs:
#     video_files = glob(os.path.join(video_dir, "*.VOB"))
#     video_files.sort(key=lambda x: int(x.split("_")[-1].split(".")[0]))
#     for video_file in video_files:
#         clip = moviepy.VideoFileClip(video_file)
#         clip.write_videofile(video_file.replace(".VOB", ".MP4"), audio=False)
#
#     print("Finished processing {}".format(video_dir))

## rename
# import os
# from tqdm import tqdm
#
# video_dir = "E:/ESD/ESD_Vessel_Frames"
# img_files = glob(os.path.join(video_dir, "*/*.png"))
# for img_file in tqdm(img_files, desc="Renaming"):
#     base_name = os.path.basename(img_file)
#     video_name = os.path.basename(os.path.dirname(img_file))
#     target_img_file = os.path.join(video_dir, video_name, base_name.replace("frame", video_name[:-8]))
#     os.rename(img_file, target_img_file)


# Save first frame of the value
from moviepy import editor

# video_dir = r"D:\ProcessedData\Vessel_Frames"
# video_files = sorted(glob(os.path.join(video_dir, "*")))  # Collect all video files
# video_files = [x for x in video_files if ".zip" not in x]
# video_names = []
# image_nums = []
# for video_file in video_files:
#     # video_file = glob(os.path.join(video_file, "*"))[0]
#     # loading video dsa gfg intro video
#     # clip = editor.VideoFileClip(video_file)
#     video_name = os.path.basename(video_file).split(".")[0]
#     video_names.append(video_name)
#     img_num = len(glob(os.path.join(video_file, "*")))
#     image_nums.append(img_num)
#     # saving a frame at 2 second
#     # clip.save_frame(r"D:\Template\TemFrames\{}.png".format(video_name), t=2)
#
# pd_data = pd.DataFrame.from_dict({"Video name": video_names, "Number of images": image_nums})
# pd_data.to_csv(r"D:\ProcessedData\Vessel_Frames\Number of images.csv", index=False)
# =======
import numpy as np
import pandas as pd
from glob import glob
from utils.tools import find_clips


# # Resoting files
# label_files = sorted(glob("./phase_all_merge/*.txt"))
# label_files = [x for x in label_files]
# phase_dict = {}
# phase_dict_key = ['idle', 'marking', 'injection', 'dissection']
# for i in range(len(phase_dict_key)):
#     phase_dict[phase_dict_key[i]] = i
#
# all_clips = {}
# data_rank = [17, 28, 16, 37, 47, 27, 30, 31, 32, 42, 38, 43, 45, 46, 44, 10, 13, 18, 7, 14, 9, 11, 15, 29, 12, 20, 22,
#              24, 23, 21, 33, 34, 35, 39, 36, 40, 41, 26, 25, 19, 5, 4, 1, 3, 2, 8, 6]
# label_files = [x for _, x in sorted(zip(data_rank, label_files))]
#
# pd_date = pd.read_csv("./case_date_days.csv")
# pd_date["File"] = label_files
# pd_date.to_csv("./case_date_days.csv", index=False)

# # Saving clips
# import os
# phase_dict_key = ['idle', 'marking', 'injection', 'dissection']
#
# pd_data = pd.read_csv("./case_date_days.csv")
# label_files = pd_data["File"].tolist()
#
# # # Get the distributions of phase clips
# data_dict = {'name': [], "frame": [],
#              'idle duration': [], 'idle clips': [], 'idle average': [],
#              'marking duration': [],  'marking clips':[], 'marking average': [],
#              'injection duration': [], 'injection clips': [], 'injection average': [],
#              'dissection duration': [], 'dissection clips': [], 'dissection average': [],}
#
# for idx, label_file in enumerate(label_files):
#     phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
#     case_name = os.path.basename(label_file).split(".")[0]
#     for phase in phase_dict_key:
#         frame_idxs = phase_label.loc[phase_label["Phase"] == phase]["Frame"].tolist()
#         if len(frame_idxs) == 0:
#             phase_clips = []
#         else:
#             phase_clips = find_clips(frame_idxs)
#             # phase_clips = [x / len(phase_label) for x in phase_clips]
#         data_dict[f"{phase} duration"].append(sum(phase_clips))
#         data_dict[f"{phase} clips"].append(len(phase_clips))
#         if len(phase_clips) == 0:
#             data_dict[f"{phase} average"].append(np.NaN)
#         else:
#             data_dict[f"{phase} average"].append(sum(phase_clips) / len(phase_clips))
#     data_dict["name"].append(case_name)
#     data_dict["frame"].append(len(phase_label["Phase"].tolist()))
#
# to_append = pd.DataFrame.from_dict(data_dict)
# pd_data = pd.concat([pd_data, to_append], axis=1, ignore_index=False)
# pd_data.to_csv("./tem.csv", index=False)

# Get transitions

import os
from sklearn import metrics

# phase_dict = {}
# phase_dict_key = ['idle', 'marking', 'injection', 'dissection']
# for i in range(len(phase_dict_key)):
#     phase_dict[phase_dict_key[i]] = i
#
# pd_data = pd.read_csv("./case_date_days.csv")
# label_files = pd_data["File"].tolist()
#
# data_dict = {"idle2marking": [], "idle2injection": [], "idle2dissection": [],
#              "marking2idle": [], "marking2injection": [], "marking2dissection": [],
#              "injection2idle": [], "injection2marking": [], "injection2dissection": [],
#              "dissection2idle": [], "dissection2marking": [], "dissection2injection": []}
# for idx, label_file in enumerate(label_files):
#     phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
#     labels = phase_label["Phase"].tolist()
#     confusion = metrics.confusion_matrix(labels[:-1], labels[1:], labels=phase_dict_key)
#     confusion_items = []
#     for i in range(len(phase_dict_key)):
#         items = confusion[i].tolist()
#         items.pop(i)
#         if sum(items) == 0:
#             confusion_items = confusion_items + [0, 0, 0]  # TODO: critical changes
#         else:
#             confusion_items = confusion_items + [x / sum(items) for x in items]  # TODO: critical changes
#
#     for k, v in zip(list(data_dict.keys()), confusion_items):
#
#         data_dict[k].append(v)
#
# pd_append = pd.DataFrame.from_dict(data_dict)
# pd_data = pd.concat([pd_data, pd_append], axis=1, ignore_index=False)
# pd_data.to_csv("./tem.csv", index=False)


# # plot points of all infos
# import matplotlib.pyplot as plt
# plt.style.use(["science", "no-latex"])
#
#
# pd_data = pd.read_csv("./stat_info.csv", header=0)
# dates = pd_data["Days"].tolist()
# for name in pd_data:
#     data = pd_data[name].tolist()
#     if isinstance(data[0], (int, float)):
#         print("Plotting {}".format(name))
#         plt.scatter(dates, data, s=5, alpha=0.8, marker="1", c="red")
#         plt.title(name)
#         plt.savefig("./stats/{}.pdf".format(name))
#         plt.clf()
#         plt.close()

# # Get correlation matrix
# import matplotlib.pyplot as plt
# plt.style.use(["science", "no-latex"])
# pd_data = pd.read_csv("./stat_info.csv", header=0)
# corr = pd_data.corr(method="pearson")
# corr = corr.applymap(lambda x: abs(x))
# corr = corr.fillna(0)
# corr = corr.style.background_gradient(cmap='Reds')
# corr.to_excel("./corr.xlsx", index=True)
# # display(corr)


# Overlay two images

#!/usr/bin/env python
# from pylab import *
# from PIL import Image
#
#
# datafile = "./test.png"
# h = Image.open(datafile)
#
# ax = axes([0,0,1,1], frameon=False)
# ax.set_axis_off()
# ax.set_xlim(0,2)
# ax.set_ylim(0,2)
# im = imshow(h, origin="upper", extent=[0, 2, 0, 2])  # axes zoom in on portion of image
# im2 = imshow(h, origin='upper',extent=[0,1,0,1]) # image is a small inset on axes
#
# >>>>>>> origin/master

# =====================================
# Save Video as images
# =====================================
# import datetime
# from moviepy.editor import VideoFileClip
#
# video_file = "/home/jeffery/hpc/Dataset/ESD_new_data/TemData/1018AnimalVideo/Bed2_case01.MP4"
# save_dir = "/home/jeffery/ProjectCode/ESDSafety/tem/case06"
# video = VideoFileClip(video_file)
# video.write_images_sequence(nameformat=os.path.join(save_dir, "%05d.png"), fps=1)
#
# img_files = sorted(glob(os.path.join(save_dir, "*")), key=lambda x: int(os.path.basename(x).split(".")[0]))
# for img_idx, img_file in enumerate(img_files):
#     base_name_str = os.path.basename(img_file).split(".")[0]
#     date = datetime.datetime.strptime("25/05/01 {}".format("0:0:0.0"),
#                                       "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=1000 * img_idx)
#     base_name_str = "{}_{}.png".format(str(img_idx+1).zfill(5), date.strftime('%H:%M:%S.%f')[:-7])
#     base_name_str = base_name_str.replace(":", "-")
#     target_img_file = os.path.join(save_dir, base_name_str)
#     os.rename(img_file, target_img_file)
# print("Finished saving {}".format(save_dir))


# Add seconds
# import datetime
# from moviepy.editor import VideoFileClip
#
# save_dir = "/media/jeffery/MedData/ESD/2022_10_18_animal_test/CaseFrames/Bed2/case07"
#
# img_files = sorted(glob(os.path.join(save_dir, "*")))
# for img_idx, img_file in enumerate(img_files, start=1):
#     base_name_str = os.path.basename(img_file).split(".")[0]
#     date = datetime.datetime.strptime("25/05/01 {}".format("0:0:0.0"),
#                                       "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=1000 * img_idx)
#     base_name_str = "{}_{}.png".format(str(img_idx).zfill(5), base_name_str)
#     # base_name_str = base_name_str.replace(":", "-")
#     target_img_file = os.path.join(save_dir, base_name_str)
#     os.rename(img_file, target_img_file)
# print("Finished saving {}".format(save_dir))

# import pandas as pd
#
# pred_file = "/media/jeffery/Luck/Tem/1018AnimalTrial/Predictions/Bed2_case05_nogui_phase.csv"
# pd_data = pd.read_csv(pred_file, header=0, sep="\t")
# pd_data["Frame"] = list(range(1, len(pd_data["Frame"].tolist()) + 1, 1))
# pd_data.to_csv(pred_file, index=False, sep="\t")

# ================================================
# Rename files
# ================================================
from moviepy.editor import VideoFileClip
import datetime

# video = VideoFileClip("/media/jeffery/MedData/ESD/2022_08_23_clinical_test/Case_B.MP4")
# print(video.duration)
# time_start = datetime.datetime.strptime("", "%H:%M:%S") - datetime.datetime.strptime("", "%H:%M:%S")

# =============================================
# Get resolutions of videos
# =============================================
# import re
# from moviepy import editor
#
# video_dirs = sorted(glob(os.path.join("/media/jeffery/MedData/ESD/ESD_data_all/video/*")))
# save_folder = "./VideoClipsLesion"
#
# datas = []
# heights = []
# widths = []
# for video_dir in video_dirs:
#     print(video_dir)
#     video_files = sorted(glob(os.path.join(video_dir, "**/**"), recursive=True))
#     try:
#         base_name = os.path.basename(video_files[-1]).split(".")[0]
#         clip = editor.VideoFileClip(video_files[-1], audio=False)
#         heights.append(clip.size[0])
#         widths.append(clip.size[1])
#         find_name = re.search("video/(.+?)/", video_files[-1])
#         if find_name:
#             video_name = find_name.group(1)
#         save_file = os.path.join(save_folder, video_name + "_" + base_name + ".mp4")
#         new_clip = clip.subclip("-10:00.00")
#         new_clip.write_videofile(save_file, audio=False, verbose=False)
#         clip.close()
#     except:
#         print("Error- {}".format(video_dir))
#         continue

# pd_data = pd.DataFrame.from_dict({"Name": datas, "Height": heights, "Width": widths})
# pd_data = pd_data.drop_duplicates(subset=["Name", "Height"])
# pd_data.to_csv("./VideoResolution.csv", index=False)


# ==================
# Get index and cases pairs
# ==================
# video_dir = "/home/jeffery/hpc/Dataset/ESD_new_data/mini_test"
# video_folders = glob(os.path.join(video_dir, "*"))
# indexs = []
# cases = []
# for video_folder in video_folders:
#     base_name = os.path.basename(video_folder).split("_")
#     if len(base_name) < 2:
#         continue
#     indexs.append(base_name[1])
#     cases.append(base_name[0])
#
# pd_data = pd.DataFrame.from_dict({"Index": indexs, "Case": cases})
# pd_data.to_csv("./IndexCase.csv", index=False)

# import re
# from moviepy.editor import VideoFileClip
# video_files = ["/media/jeffery/MedData/ESD/ESD_data_all/video/22_E8188630_20101014/VTS_01_4.VOB"]
# for video_file in video_files:
#     try:
#         base_name = os.path.basename(video_file).split(".")[0]
#         clip = VideoFileClip(video_file, audio=False)
#         clip.write_videofile("{}.mp4".format(base_name), audio=False, verbose=False)
#         clip.close()
#     except:
#         print("Error- {}".format(video_file))
#         continue

# ==================================
# Save images around dissection
# ==================================
# import shutil
# image_dir = "/home/jeffery/hpc/Dataset/ESD_new_data/mini_test"
# save_dir = "VideoSizeFolder"
# video_label_files = sorted(glob("/home/jeffery/hpc/Dataset/ESD_new_data/phase_all_merge/*.txt"))
# for video_label_file in tqdm(video_label_files):
#     video_name = os.path.basename(video_label_file).split(".")[0]
#     img_files = sorted(glob(os.path.join(image_dir, video_name, "*")))
#     img_files.sort(key=lambda x: int(x.split("-")[-1].split(".")[0]))
#     pd_label0 = pd.read_csv(video_label_file, header=None, sep="\t")
#     pd_label0.columns = ["Frame", "Phase"]
#     pd_label = pd_label0[pd_label0["Phase"] == "dissection"]
#     first_dissection_frame = pd_label["Frame"].tolist()[0]
#     sample_start = max(0, first_dissection_frame - 180)
#     sample_end = min(len(pd_label0), first_dissection_frame + 180)
#     save_images = img_files[sample_start:sample_end]
#     save_folder = os.path.join(save_dir, video_name)
#     if not os.path.isdir(save_folder):
#         os.makedirs(save_folder)
#     else:
#         shutil.rmtree(save_folder)
#         os.makedirs(save_folder)
#     for save_image in save_images:
#         new_image = os.path.join(save_folder, os.path.basename(save_image))
#         shutil.copy(save_image, new_image)
#
#     print("Finish {}".format(video_name))
#
# video_files = sorted(glob("./VideoSizeFolder/*"))
# video_names = [os.path.basename(x).split(".")[0] for x in video_files]
# pd_data = pd.DataFrame.from_dict({"Case": video_names})
# pd_data["Width"] = ""
# pd_data["Height"] = ""
# pd_data.to_csv("./Lesion_log.csv", index=False)


# ===============================
# Downsample images
# ===============================
# import multiprocessing as mp
# def dowsample(video_file):
#     save_dir = "/home/jeffery/Downloads/OtherEquipFrames"
#     base_name = os.path.basename(video_file).split(".")[0].replace(" ", "-")
#     save_dir = os.path.join(save_dir, base_name)
#     if not os.path.isdir(save_dir):
#         os.makedirs(save_dir)
#
#     clip = editor.VideoFileClip(video_file, audio=False)
#     clip.write_images_sequence(nameformat=os.path.join(save_dir, base_name + "-" +"-%05d.png"), fps=1)
#     clip.close()
#
# if __name__ == "__main__":
#     mpPool = mp.Pool(10)
#     video_files = glob("/home/jeffery/Downloads/OtherEquip/*")
#     mpPool.map(dowsample, video_files)
#     mpPool.close()
#     mpPool.join()

# import os
# from PIL import Image
# import numpy as np
# from tqdm import tqdm
# import matplotlib.pyplot as plt
# from glob import glob
#
# img_dir = "/media/jeffery/MedData/ESD/Data4NCResponse/OtherEquipFrames/Pocket-creation-method-Dr-Hironori-Yamamoto"
# img_files = sorted(glob(os.path.join(img_dir, "*")))
# for img_file in tqdm(img_files[98:]):
#     img = Image.open(img_file)
#     img = np.array(img)[:, 10:]
#     img = Image.fromarray(img)
#     img.save(img_file)
#
# #
# img_file = "/media/jeffery/MedData/ESD/Data4NCResponse/OtherEquipFrames/Pocket-creation-method-Dr-Hironori-Yamamoto/Pocket-creation-method-Dr-Hironori-Yamamoto--00701.png"
# img = Image.open(img_file)
# img = np.array(img)[10: 350, 260:650]
# plt.imshow(img)
# plt.show()


# =========================================
# Select all images of injection
# =========================================
# label_file = "/home/jeffery/hpc/Dataset/ESD_new_data/phase_all_merge/Case40_37_A199_18_5_2019.txt"
# img_files = glob("/home/jeffery/hpc/Dataset/ESD_new_data/mini_test/Case40_37_A199_18_5_2019/*")
# img_files = sorted(img_files, key=lambda x: int(os.path.basename(x).split("-")[-1].split(".")[0]))
# save_folder = "/home/jeffery/Downloads/TumorSizeCheck/Case40_37_A199_18_5_2019"
#
# # read label
# phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
# phase_label["Frame"] = list(range(1, len(phase_label) + 1, 1))
# frame_idxs = phase_label[phase_label["Phase"] == "marking"]["Frame"].tolist()
# for frame_idx in tqdm(frame_idxs, desc=label_file):
#     img_file = img_files[frame_idx-1]
#     save_file = os.path.join(save_folder, os.path.basename(img_file))
#     shutil.copy(img_file, save_file)


# ============================================
# List folder
# ============================================
# list_folders = glob(os.path.join("/media/jeffery/MedData/ESD/NewData_2022_12_22", "*"))
# list_folders = [os.path.basename(x) for x in list_folders if os.path.isdir(x)]
# list_folders = sorted(list_folders)
# save_file = "/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/log.xlsx"
# pd_log = pd.DataFrame.from_dict({"Name": list_folders})
# pd_log.to_excel(save_file, index=False)





# ================================
# Rename files
# ================================
# import shutil
# for case in ["ESD_Barret003", "ESD_Barrett002", "ESD_Magen002", "ESD_Rektum009"]:
#     img_files = sorted(glob(os.path.join("/home/jeffery/ProjectData/MarkusData/{}/*".format(case))))
#     for idx, img_file in enumerate(tqdm(img_files), start=1):
#         base_name = os.path.basename(os.path.dirname(img_file))
#         target_file = os.path.join(os.path.dirname(img_file), "{}-{}.png".format(base_name, str(idx).zfill(5)))
#         shutil.move(img_file, target_file)


# ==================================================
# Combine videos
# ==================================================
# from moviepy.editor import VideoFileClip, concatenate_videoclips
# data_root = "/home/jeffery/Downloads/Honchi_Techni"
# data_dirs = glob(os.path.join(data_root, "*"))
# for data_dir in tqdm(data_dirs, desc="Combining videos"):
#     data_files = sorted(glob(os.path.join(data_dir, "**/*.MP4"), recursive=True))
#     clips = []
#     for data_file in data_files:
#         clip = VideoFileClip(data_file, audio=False)
#         clips.append(clip)
#     video = concatenate_videoclips(clips)
#     video.write_videofile(os.path.join(data_dir, os.path.basename(data_dir) + ".MP4"), audio=False)


# =======================================
# Get frame samples of data
# =======================================
# from moviepy.editor import VideoFileClip
# from PIL import Image
# pd_log = pd.read_excel("/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/log.xlsx")
# save_sample_folder = "/home/jeffery/hpc/Dataset/ESD_new_data/Backup/SampleFrame"
# pd_log = pd_log.fillna("")
# # pd_log = pd_log[pd_log["Name"] == "20220908141442_0000_k3317218"]
# for idx, row in pd_log.iterrows():
#     data_name = row["Name"]
#     try:
#         if len(row["Note"]) != 0:
#             continue
#         if "," in str(row["Selected"]):
#             video_idxs = [int(s) for s in row["Selected"].split(",")]
#         else:
#             video_idxs = [row["Selected"]]
#         all_files = glob(os.path.join("/media/jeffery/MedData/ESD/NewData_2022_12_22", data_name, "**/**"), recursive=True)
#         video_files0 = [video_file for video_file in all_files if os.path.isfile(video_file)]
#         video_files0 = sorted(list(set(video_files0)))
#         video_files = [video_files0[ix] for ix in video_idxs]
#         sample_video_file = video_files[0]
#         clip = VideoFileClip(sample_video_file)
#         frame = clip.get_frame(100)
#         save_file = os.path.join(save_sample_folder, "{}_100.png".format(data_name))
#         img = Image.fromarray(frame)
#         img.save(save_file)
#         clip.close()
#     except:
#         print(data_name)

# ==================================================
# Downsample images as video
# ==================================================
# import shutil
# from tqdm import tqdm
# import multiprocessing as mp
# from moviepy.video.fx import all
#
#
# def downsample_videos(row):
#     data_name = row["Name"]
#     case_folder = os.path.join(save_folder, data_name)
#     os.makedirs(case_folder, exist_ok=True)
#
#     if isinstance(row["Selected"], int):
#         video_idxs = [row["Selected"]]
#     else:
#         video_idxs = [int(s) for s in row["Selected"].split(",")]
#     video_files = glob(os.path.join("/media/jeffery/MedData/ESD/NewData_2022_12_22", data_name, "**/**"), recursive=True)
#     video_files = [video_file for video_file in video_files if os.path.isfile(video_file)]
#     video_files = sorted(list(set(video_files)))
#     video_files = [video_files[idx0] for idx0 in video_idxs]
#     clips = []
#     for video_file in video_files:
#         clip = editor.VideoFileClip(video_file, audio=False)
#         clips.append(clip)
#         # clip.close()
#
#     whole_video = editor.concatenate_videoclips(clips)
#     # frame = whole_video.get_frame(10)
#     # sw, sh, sc = frame.shape
#     p1, p2, p3, p4 = [int(x) for x in [row["Point1"], row["Point2"], row["Point3"], row["Point4"]]]
#
#     target_video = all.crop(whole_video, x1=p1, y1=p2, x2=p3, y2=p4)
#     target_video = target_video.resize(0.5)
#     target_video.write_images_sequence(nameformat=os.path.join(case_folder, "frame-%05d.png"), fps=1)
#
#     whole_video.close()
#     print("Finished {}".format(data_name))
#
#
# if __name__ == "__main__":
#     log_file = "/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/log.xlsx"
#     pd_log = pd.read_excel(log_file)
#     pd_log = pd_log.fillna("")
#     pd_log = pd_log[pd_log["Point1"] != ""]
#     pd_log = pd_log[pd_log["Downsampled"] == ""]
#     save_folder = "/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/Images"
#
#     mpPool = mp.Pool(mp.cpu_count() - 1)
#     configs = []
#     for idx, row in tqdm(pd_log.iterrows(), total=len(pd_log)):
#         configs.append(row)
#         # downsample_videos(configs[-1])
#     for idx, _ in enumerate(tqdm(mpPool.imap_unordered(downsample_videos, configs), total=len(configs), desc="Downsample videos")):
#         pass


# ======================================
# Check frames
# ======================================
# root_dir = "/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/Images"
# save_dir = "/home/jeffery/hpc/Dataset/ESD_new_data/Backup/CheckedFrames"
# data_folders = glob(os.path.join(root_dir, "*"))
#
# for data_folder in tqdm(data_folders):
#     img_files = glob(os.path.join(data_folder, "*"))
#     img_file = img_files[10]
#     data_name = os.path.basename(data_folder)
#     shutil.copy(img_file, os.path.join(save_dir, data_name + ".png"))

# ================================
# Sort out stastical information
# ================================
def find_info(pd_data, query_str, query_col):
    for _, check_row in pd_data.iterrows():
        if query_str in check_row["HKID"].lower():
            return check_row[query_col]
    return ""



raw_info = "/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/Yip_ESD_Aug_2022.xlsx"
processed_info = "/home/jeffery/hpc/Dataset/ESD_new_data/20221222NewCases/log.xlsx"
pd_raw_info = pd.read_excel(raw_info)
pd_processed = pd.read_excel(processed_info)

pd_raw_info = pd_raw_info.fillna("")
pd_raw_info = pd_raw_info[pd_raw_info["Name"] != ""]

dates = []
surgeons = []
procedures = []

for _, row in pd_processed.iterrows():
    id = row["Name"][-4:].lower()
    dates.append(find_info(pd_raw_info, id, "Date"))
    surgeons.append(find_info(pd_raw_info, id, "D/B"))
    procedures.append(find_info(pd_raw_info, id, "Procedure"))

pd_processed.insert(1, "Date", dates)
pd_processed.insert(2, "Surgeon", surgeons)
pd_processed.insert(3, "Procedure", procedures)
pd_processed.to_excel(processed_info.replace(".xlsx", "_refine.xlsx"), index=False)
