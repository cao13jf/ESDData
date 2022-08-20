

# # Analysis clip features in annotations
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

from utils.tools import find_clips

plt.style.use(["science", "no-latex"])


# ===============================
# Collect the number of phase clips
# ===============================

label_files = sorted(glob("/Users/jeff/Downloads/phase_all_merge/*.txt"))
label_files = [x for x in label_files]
phase_dict = {}
phase_dict_key = ['idle', 'marking', 'injection', 'dissection']
for i in range(len(phase_dict_key)):
    phase_dict[phase_dict_key[i]] = i

all_clips = {}
data_rank = [17, 28, 16, 37, 47, 27, 30, 31, 32, 42, 38, 43, 45, 46, 44, 10, 13, 18, 7, 14, 9, 11, 15, 29, 12, 20, 22,
             24, 23, 21, 33, 34, 35, 39, 36, 40, 41, 26, 25, 19, 5, 4, 1, 3, 2, 8, 6]
label_files = [x for _, x in sorted(zip(data_rank, label_files))]

# # Get the distributions of phase clips
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
            # phase_clips = [x / len(phase_label) for x in phase_clips]
        clip_cunts[phase] = len(phase_clips)
        clip_cunts["{} frame".format(phase)] = sum(phase_clips)
    clip_cunts["total"] = len(phase_label["Phase"].tolist())
    all_clips[case_name] = clip_cunts

data_dict = {"Rank": [], "Name": [], "Injection": [], "Dissection": [], "Injection frame": [], "Dissection frame":[], "Injection ratio": [], "Dissection ratio": []}
rank = 1
for k, v in all_clips.items():
    data_dict["Rank"].append(rank)
    data_dict["Name"].append(k)
    data_dict["Injection"].append(v["injection"])
    data_dict["Dissection"].append(v["dissection"])
    data_dict["Injection frame"].append(v["injection frame"])
    data_dict["Injection ratio"].append(v["injection"] / v["injection frame"])
    data_dict["Dissection frame"].append(v["dissection frame"])
    data_dict["Dissection ratio"].append(v["dissection"] / v["dissection frame"])
    rank += 1

data_pd = pd.DataFrame.from_dict(data_dict)
data_pd.to_csv("/Users/jeff/Downloads/injection_and_dissection.csv", index=False)


# ======================================
# Plot distribution of phase clips
# ======================================
# for phase in phase_dict_key:
#     print(phase)
#     each_phase_clips = []
#     for k, v in all_clips.items():
#         each_phase_clips.append(v[phase])
#
#     fig, ax = plt.subplots()
#     ax.boxplot(each_phase_clips)
#     # plt.setp(ax.get_xticklabels(), rotation=-10, ha="left", rotation_mode="anchor", labelsize=4)
#     every_nth = 5
#     for n, label in enumerate(ax.xaxis.get_ticklabels(), start=1):
#         if n % every_nth != 0:
#             label.set_visible(False)
#     plt.minorticks_off()
#     plt.grid(axis='y')
#     plt.title("Clip distribution of phase {}".format(phase))
#     plt.savefig("/Users/jeff/Downloads/clip_{}.pdf".format(phase))
#     plt.clf()
#     plt.close()


# ===============================
# Get transformation between different clips
# ===============================

# # Get phase transformation frequency
from sklearn import metrics
from utils.tools import heatmap, annotate_heatmap

# for idx, label_file in enumerate(label_files):
#     case_name = os.path.basename(label_file).split(".")[0]
#     phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
#     # phase_label = phase_label.replace({"Phase": phase_dict})
#     labels = phase_label["Phase"].tolist()
#     trans_matrix = metrics.confusion_matrix(labels[:-1], labels[1:], labels=phase_dict_key, normalize=None)
#     for i in range(len(phase_dict_key)):
#         trans_matrix[i, i] = 0
#     fig, ax = plt.subplots()
#     im, cbar = heatmap(trans_matrix, phase_dict_key, phase_dict_key, ax)
#     texts = annotate_heatmap(im, valfmt="{x:.2f}")
#     # fig.tight_layout()
#     plt.ylabel("Source frame")
#     # pstr = "Prediction {}; acc {:>10.4f}".format(base_name.split("_")[0], acc)
#     plt.xlabel("Target frame")
#     plt.savefig("/Users/jeff/Downloads/TransMatrix/trans_oroder-{}_{}.pdf".format(idx, case_name))
#     plt.clf()
#     plt.close()

# # Get transition curves
# from sklearn import metrics
# from utils.tools import heatmap, annotate_heatmap
#
# curves = []
# for idx, label_file in enumerate(label_files):
#     case_name = os.path.basename(label_file).split(".")[0]
#     phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
#     # phase_label = phase_label.replace({"Phase": phase_dict})
#     labels = phase_label["Phase"].tolist()
#     trans_matrix = metrics.confusion_matrix(labels[:-1], labels[1:], labels=phase_dict_key, normalize=None)
#     for i in range(len(phase_dict_key)):
#         trans_matrix[i, i] = 0
#     items = trans_matrix.flatten().tolist()
#     curves.append(items)
#
# curves.pop(0); curves.pop(4); curves.pop(8); curves.pop(12)
# # preserved curves
# curves = list(zip(*curves))
# for idx, curve in enumerate(curves, start=0):
#     source_phase = phase_dict_key[idx // 4]
#     target_phase = phase_dict_key[idx % 4]
#     fig, ax = plt.subplots()
#     ax.plot(list(range(1, len(curve) + 1)), curve, label="Index {}".format(idx))
#     # plt.legend()
#     # ax.get_legend().remove()
#     plt.title("{}_2_{}".format(source_phase, target_phase))
#     plt.savefig("/Users/jeff/Downloads/TransMatrix/trans_curve_{}.pdf".format(str(idx).zfill(2)))
#     plt.clf()
#     plt.close()




