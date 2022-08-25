"""
Save video as downsampled image sequence
"""
# # Combien multiple videos
import os
from glob import glob
from moviepy import editor
import multiprocessing as mp

def downsample2image(video_dir, target_fps=1):

    print("Begin {}".format(video_dir))
    save_dir = os.path.join(r"D:\ProcessedData\RawVideo1FPS", os.path.basename(video_dir))
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

        # # Reading videos
    video_files = sorted(glob(os.path.join(video_dir, "*")),
                         key=lambda x: int(x.split("_")[-1].split(".")[0]))  # Collect all video files
    clips = []
    for video_file in video_files:
        clip = editor.VideoFileClip(video_file, audio=False)
        clips.append(clip)
    whole_video = editor.concatenate_videoclips(clips)
    # # save downsample image
    whole_video.write_images_sequence(nameformat=os.path.join(save_dir, "frame-%05d.png"), fps=target_fps, logger=None)


if __name__ == "__main__":
    data_names = ["42_G316314"]
    video_dir = r"D:\Download"
    video_dirs = [os.path.join(video_dir, x) for x in data_names]
    downsample2image(video_dirs[0])
    mpPool = mp.Pool(len(data_names))
    mpPool.map(downsample2image, video_dirs)
    mpPool.close()
    mpPool.join()
