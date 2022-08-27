"""
Save video as downsampled image sequence
"""
# # Combien multiple videos
import os
import datetime
from glob import glob
from moviepy import editor
from moviepy.video.fx import resize
import multiprocessing as mp

def downsample2image(config):
    video_file = config["video_file"]
    target_fps = config["target_fps"]
    start_time = config["start_time"]

    print("Begin {}".format(video_file))
    save_dir = config["save_dir"]
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    whole_video = editor.VideoFileClip(video_file, audio=False)
    whole_video = whole_video.resize(0.5)
    # # save downsample image
    whole_video.write_images_sequence(nameformat=os.path.join(save_dir, "frame-%05d.png"), fps=target_fps, logger=None)

    img_files = sorted(glob(os.path.join(save_dir, "frame-*.png")))
    for idx, img_file in enumerate(img_files):
        base_name_str = os.path.basename(img_file).split("-")[-1].split(".")[0]
        date = datetime.datetime.strptime("25/05/01 {}".format(start_time), "%d/%m/%y %H:%M:%S.%f") + datetime.timedelta(milliseconds=1000*idx)
        base_name_time = date.strftime('%H:%M:%S.%f')[:-7]
        base_name_time = base_name_time.replace(":", "_")
        target_img_file = os.path.join(save_dir, os.path.basename(img_file).replace(base_name_str, base_name_time))
        os.rename(img_file, target_img_file)
    print("Finished processing {}".format(save_dir))


if __name__ == "__main__":
    data_names = ["42_G316314"]
    video_dir = r"D:\Download"
    video_dirs = [os.path.join(video_dir, x) for x in data_names]
    downsample2image(video_dirs[0])
    mpPool = mp.Pool(len(data_names))
    mpPool.map(downsample2image, video_dirs)
    mpPool.close()
    mpPool.join()
