import os
import shutil
import argparse
import cv2
import math
from lxml import etree
import numpy as np
from PIL import Image

P = [252, 233, 79, 114, 159, 207, 239, 41, 41, 173, 127, 168, 138, 226, 52,
     233, 185, 110, 252, 175, 62, 211, 215, 207, 196, 160, 0, 32, 74, 135, 164, 0, 0,
     92, 53, 102, 78, 154, 6, 143, 89, 2, 206, 92, 0, 136, 138, 133, 237, 212, 0, 52,
     101, 164, 204, 0, 0, 117, 80, 123, 115, 210, 22, 193, 125, 17, 245, 121, 0, 186,
     189, 182, 85, 87, 83, 46, 52, 54, 238, 238, 236, 0, 0, 10, 252, 233, 89, 114, 159,
     217, 239, 41, 51, 173, 127, 178, 138, 226, 62, 233, 185, 120, 252, 175, 72, 211, 215,
     217, 196, 160, 10, 32, 74, 145, 164, 0, 10, 92, 53, 112, 78, 154, 16, 143, 89, 12,
     206, 92, 10, 136, 138, 143, 237, 212, 10, 52, 101, 174, 204, 0, 10, 117, 80, 133, 115,
     210, 32, 193, 125, 27, 245, 121, 10, 186, 189, 192, 85, 87, 93, 46, 52, 64, 238, 238, 246]

P = P * math.floor(255*3/len(P))
l = int(255 - len(P)/3)
P = P + P[3:(l+1)*3]
P = [0,0,0] + P

def save_indexed_png(fname, label_map, palette=P):
    if label_map.max() > 255:
        label_map = np.remainder(label_map, 255)
    label_map = np.squeeze(label_map.astype(np.uint8))
    im = Image.fromarray(label_map, 'P')
    im.putpalette(palette)
    im.save(fname, 'PNG')


def dir_create(path):
    if (os.path.exists(path)) and (os.listdir(path) != []):
        shutil.rmtree(path)
        os.makedirs(path)
    if not os.path.exists(path):
        os.makedirs(path)

def parse_anno_file(cvat_xml, image_name):
    root = etree.parse(cvat_xml).getroot()
    anno = []

    image_name_attr = ".//image[@name='{}']".format(image_name)
    for image_tag in root.iterfind(image_name_attr):
        image = {}
        for key, value in image_tag.items():
            image[key] = value
        image['shapes'] = []
        for poly_tag in image_tag.iter('polyline'):
            polygon = {'type': 'polygon'}
            for key, value in poly_tag.items():
                polygon[key] = value
            image['shapes'].append(polygon)
        for box_tag in image_tag.iter('box'):
            box = {'type': 'box'}
            for key, value in box_tag.items():
                box[key] = value
            box['points'] = "{0},{1};{2},{1};{2},{3};{0},{3}".format(
                box['xtl'], box['ytl'], box['xbr'], box['ybr'])
            image['shapes'].append(box)
        image['shapes'].sort(key=lambda x: int(x.get('z_order', 0)))
        anno.append(image)
    return anno

def create_mask_file(mask, polygon, label):
    points = [tuple(map(float, p.split(','))) for p in polygon.split(';')]
    points = np.array([(int(p[0]), int(p[1])) for p in points])
    points = points.astype(int)
    # mask = cv2.drawContours(mask, [points], -1, color=(255, 255, 255), thickness=5)
    height, width = mask.shape
    mask_array = np.zeros((height, width, 3), dtype=np.uint8)  # TODO: check hight and width
    mask_array = cv2.fillPoly(mask_array, [points], color=(0, 0, 255))
    mask[mask_array[..., -1] != 0] = label

    return mask


def find_clips(frame_idxs):
    clip_durations = []  # [[start1, end1], ...]
    gaps = [right - left for left, right in zip(frame_idxs[:-1], frame_idxs[1:])]

    duration = [frame_idxs[0]]
    for idx, gap in enumerate(gaps):
        if gap > 1:
            duration.append(frame_idxs[idx])
            clip_durations.append(duration[1] - duration[0])
            duration = [frame_idxs[idx + 1]]
    duration.append(frame_idxs[-1])
    clip_durations.append(duration[1] - duration[0])

    return clip_durations
