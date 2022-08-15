

# # Analysis clip features in annotations
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

from utils.tools import find_clips

plt.style.use(["science", "no-latex"])

label_files = sorted(glob("/Users/jeff/Downloads/phase_all_merge/*.txt"))[:40]
phase_dict = {}
phase_dict_key = ['idle', 'marking', 'injection', 'dissection']
for i in range(len(phase_dict_key)):
    phase_dict[phase_dict_key[i]] = i


all_clips = {}

for idx, label_file in enumerate(label_files):
    phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
    case_name = os.path.basename(label_file).split(".")[0]
    clip_cunts = {'idle': [], 'marking': [], 'injection': [], 'dissection': []}
    for phase in phase_dict_key:
        frame_idxs = phase_label.loc[phase_label["Phase"] == phase]["Frame"].tolist()
        if len(frame_idxs) == 0:
            phase_clips = []
        else:
            phase_clips = find_clips(frame_idxs)
        clip_cunts[phase] = phase_clips
    all_clips[case_name] = clip_cunts

for phase in phase_dict_key:
    print(phase)
    each_phase_clips = []
    for k, v in all_clips.items():
        each_phase_clips.append(v[phase])

    fig, ax = plt.subplots()
    ax.violinplot(each_phase_clips)
    plt.setp(ax.get_xticklabels(), rotation=-10, ha="left", rotation_mode="anchor")
    plt.minorticks_off()
    plt.grid(axis='y')
    plt.savefig("/Users/jeff/Downloads/{}_clip.pdf".format(phase))
    plt.clf()
    plt.close()