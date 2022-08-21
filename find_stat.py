

# # Analysis clip features in annotations
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

from utils.tools import find_clips

plt.style.use(["science", "no-latex"])

label_files = sorted(glob("/Users/jeff/Downloads/phase_all_merge/*.txt"))
label_files = [x for x in label_files]
phase_dict = {}
phase_dict_key = ['idle', 'marking', 'injection', 'dissection']
for i in range(len(phase_dict_key)):
    phase_dict[phase_dict_key[i]] = i
data_rank = [17, 28, 16, 37, 47, 27, 30, 31, 32, 42, 38, 43, 45, 46, 44, 10, 13, 18, 7, 14, 9, 11, 15, 29, 12, 20, 22,
             24, 23, 21, 33, 34, 35, 39, 36, 40, 41, 26, 25, 19, 5, 4, 1, 3, 2, 8, 6]
data_year = [2014, 2016, 2014, 2019, 2020, 2016, 2016, 2017, 2017, 2019, 2019, 2019, 2019, 2020, 2019, 2012, 2013, 2015,
             2008, 2013, 2010, 2012, 2013, 2016, 2012, 2015, 2016, 2016, 2016, 2016, 2017, 2017, 2018, 2019, 2019, 2019,
             2019, 2016, 2016, 2015, 2008, 2008, 2008, 2008, 2008, 2009, 2008]

label_files = [x for x_rank, x in sorted(zip(data_rank, label_files)) if x_rank not in [17, 13, 18, 14, 29, 40, 19, 4, 2, 8, 6]]
data_year = [x for x_rank, x in sorted(zip(data_rank, data_year)) if x_rank not in [17, 13, 18, 14, 29, 40, 19, 4, 2, 8, 6]]

def add2dict(data_dict, key, value):
    if key in data_dict:
        data_dict[key] = data_dict[key] + [value]
    else:
        data_dict[key] = [value]

    return data_dict

# ===============================
# Collect the number of phase durations
# ===============================
# phase_durations = {"year": [], 'idle': [], 'marking': [], 'injection': [], 'dissection': []}
#
# all_clips = {}
# for idx, label_file in enumerate(label_files):
#     phase_durations["year"].append(data_year[idx])
#     phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
#     case_name = os.path.basename(label_file).split(".")[0]
#     for phase in phase_dict_key:
#         frame_idxs = phase_label.loc[phase_label["Phase"] == phase]["Frame"].tolist()
#         phase_durations[phase].append(len(frame_idxs) / len(phase_label["Frame"].tolist()))
#
# phase = "injection"
# year_clips = [[phase_durations[phase][0]]]
# years = [phase_durations["year"][0]]
# for idx, idx_year in enumerate(phase_durations["year"][1:]):
#     if idx_year == years[-1]:
#         year_clips[-1].append(phase_durations["injection"][idx+1] / phase_durations["dissection"][idx+1])
#     else:
#         years.append(idx_year)
#         year_clips.append([phase_durations["injection"][idx+1] / phase_durations["dissection"][idx+1]])
#
# fig, ax = plt.subplots()
# ax.boxplot(year_clips, labels=years)
# plt.setp(ax.get_xticklabels(), rotation=40, ha="left", rotation_mode="anchor")
# # plt.setp(ax.get_xticklabels(), rotation=-10, ha="left", rotation_mode="anchor", labelsize=4)
# # every_nth = 5
# # for n, label in enumerate(ax.xaxis.get_ticklabels(), start=1):
# #     if n % every_nth != 0:
# #         label.set_visible(False)
# plt.title("injection / dissection")
# plt.minorticks_off()
# plt.grid(axis='y')
# # plt.show()
# plt.savefig("/Users/jeff/PaperWritting/EndoAI/FindScore/{}_proportion.pdf".format(phase))


# ===============================
# Collect the number of phase distributions
# ===============================
phase_durations = {"year": [], 'idle': [], 'marking': [], 'injection': [], 'dissection': []}

all_clips = {}
for idx, label_file in enumerate(label_files):
    phase_durations["year"].append(data_year[idx])
    phase_label = pd.read_csv(label_file, header=None, sep="\t", names=["Frame", "Phase"], index_col=False)
    case_name = os.path.basename(label_file).split(".")[0]
    for phase in phase_dict_key:
        frame_idxs = phase_label.loc[phase_label["Phase"] == phase]["Frame"].tolist()
        if len(frame_idxs) != 0:
            phase_durations[phase].append(find_clips(frame_idxs))
        else:
            phase_durations[phase].append([])

phase = "dissection"
year_clips = [phase_durations[phase][0]]
years = [phase_durations["year"][0]]
for idx, idx_year in enumerate(phase_durations["year"][1:]):
    if idx_year == years[-1]:
        year_clips[-1] = year_clips[-1] + phase_durations[phase][idx+1]
    else:
        years.append(idx_year)
        year_clips.append(phase_durations[phase][idx+1])
norm_clips = []
for clip in year_clips:
    clip_sum = len(clip)
    norm_clip = [x / clip_sum for x in clip]
    norm_clips.append(norm_clip)

# phase = "injection"
# injection_year_clips = [phase_durations[phase][0]]
# years = [phase_durations["year"][0]]
# for idx, idx_year in enumerate(phase_durations["year"][1:]):
#     if idx_year == years[-1]:
#         injection_year_clips[-1] = injection_year_clips[-1] + phase_durations[phase][idx+1]
#     else:
#         years.append(idx_year)
#         injection_year_clips.append(phase_durations[phase][idx+1])
#
# phase = "dissection"
# dissection_year_clips = [phase_durations[phase][0]]
# years = [phase_durations["year"][0]]
# for idx, idx_year in enumerate(phase_durations["year"][1:]):
#     if idx_year == years[-1]:
#         dissection_year_clips[-1] = dissection_year_clips[-1] + phase_durations[phase][idx+1]
#     else:
#         years.append(idx_year)
#         dissection_year_clips.append(phase_durations[phase][idx+1])
#
# norm_clips = []
# for injection_clip, dissection_clip in zip(injection_year_clips, dissection_year_clips):
#     injection_clip_sum = len(injection_clip)
#     norm_inejction_clip = [x / injection_clip_sum for x in injection_clip]
    #     dissection_clip_sum = len(dissection_clip)
#     norm_dissection_clip = [x / dissection_clip_sum for x in dissection_clip]
#     norm_clips.append([x / y for x, y in zip(norm_inejction_clip, norm_dissection_clip)])

fig, ax = plt.subplots()
ax.boxplot(norm_clips, labels=years)
plt.setp(ax.get_xticklabels(), rotation=40, ha="left", rotation_mode="anchor")
# plt.setp(ax.get_xticklabels(), rotation=-10, ha="left", rotation_mode="anchor", labelsize=4)
# every_nth = 5
# for n, label in enumerate(ax.xaxis.get_ticklabels(), start=1):
#     if n % every_nth != 0:
#         label.set_visible(False)
plt.title("Distribution of {} clips".format(phase))
plt.minorticks_off()
plt.grid(axis='y')
# plt.show()
plt.savefig("/Users/jeff/PaperWritting/EndoAI/FindScore/distribution_{}.pdf".format(phase))
