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

save_dir = r"F:\ESD\ESD_Vessel_Frames\15_A97001983_clipped"

img_files = sorted(glob(os.path.join(save_dir, "frame-*.png")))
img_files = [img_file for img_file in img_files if "_" not in os.path.basename(img_file)]

for idx, img_file in enumerate(img_files, start=198):
    base_name_str = os.path.basename(img_file).split("-")[-1].split(".")[0]  # frame-00_13_22-1
    date = datetime.datetime.strptime("25/05/01 00:0:0.0", "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=500*idx)
    base_name_time = date.strftime('%H:%M:%S.%f')[:-4]
    base_name_time = base_name_time.replace(":", "_").replace(".00", "-1")
    base_name_time = base_name_time.replace(":", "_").replace(".50", "-2")
    target_img_file = os.path.join(save_dir, os.path.basename(img_file).replace(base_name_str, base_name_time))
    os.rename(img_file, target_img_file)
print("Finished processing {}".format(save_dir))


