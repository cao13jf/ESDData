import os
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

video_dir = r"D:\ProcessedData\Vessel_Frames"
video_files = sorted(glob(os.path.join(video_dir, "*")))  # Collect all video files
video_files = [x for x in video_files if ".zip" not in x]
video_names = []
image_nums = []
for video_file in video_files:
    # video_file = glob(os.path.join(video_file, "*"))[0]
    # loading video dsa gfg intro video
    # clip = editor.VideoFileClip(video_file)
    video_name = os.path.basename(video_file).split(".")[0]
    video_names.append(video_name)
    img_num = len(glob(os.path.join(video_file, "*")))
    image_nums.append(img_num)
    # saving a frame at 2 second
    # clip.save_frame(r"D:\Template\TemFrames\{}.png".format(video_name), t=2)

pd_data = pd.DataFrame.from_dict({"Video name": video_names, "Number of images": image_nums})
pd_data.to_csv(r"D:\ProcessedData\Vessel_Frames\Number of images.csv", index=False)