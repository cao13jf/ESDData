# refer to https://towardsdatascience.com/extract-annotations-from-cvat-xml-file-into-mask-files-in-python-bb69749c4dc9

import os
import cv2
import argparse
import numpy as np
from tqdm import tqdm

from utils.utils import dir_create, parse_anno_file, create_mask_file, save_indexed_png

label2num = {"a": 1, "b": 2, "c": 3}  # TODO: Change label dicationary

def parse_args():
    parser = argparse.ArgumentParser(
        fromfile_prefix_chars='@',
        description='Convert CVAT XML annotations to contours'
    )
    parser.add_argument(
            '--image-dir', metavar='DIRECTORY', required=True,
            help='directory with input images'
        )

    parser.add_argument(
            '--cvat-xml', metavar='FILE', required=True,
            help='input file with CVAT annotation in xml format'
        )
    parser.add_argument(
            '--output-dir', metavar='DIRECTORY', required=True,
            help='directory for output masks'
        )

    return parser.parse_args()

def main():
    args = parse_args()
    dir_create(args.output_dir)
    img_list = [f for f in os.listdir(args.image_dir) if os.path.isfile(os.path.join(args.image_dir, f))]
    for img in tqdm(img_list, desc='Writing contours:'):
        if "765" in img:
            print("test")
        anno = parse_anno_file(args.cvat_xml, img)
        output_path = os.path.join(args.output_dir, img.split('.')[0] + '_mask.png')
        mask = np.zeros((int(anno[0]["height"]), int(anno[0]["width"]))).astype(np.uint8)
        if len(anno[0]["shapes"]) != 0:
            for shape in anno[0]["shapes"]:
                mask = create_mask_file(mask,
                                        shape["points"],
                                        label=label2num[shape["label"]])
        save_indexed_png(output_path, mask)

if __name__ == "__main__":
    main()