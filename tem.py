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


# plot points of all infos
import matplotlib.pyplot as plt
plt.style.use(["science", "no-latex"])


pd_data = pd.read_csv("./stat_info.csv", header=0)
dates = pd_data["Days"].tolist()
for name in pd_data:
    data = pd_data[name].tolist()
    if isinstance(data[0], (int, float)):
        print("Plotting {}".format(name))
        plt.scatter(dates, data)
        plt.title(name)
        plt.savefig("./stats/{}.pdf".format(name))
        plt.clf()
        plt.close()



