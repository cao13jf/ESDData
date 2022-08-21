import os.path

import numpy as np
from matplotlib.pyplot import figure
from matplotlib import pyplot as plt
from PIL import Image

from utils.tools import generate_phase_band, get_durations, plot_pie, generate_transition

# overlaid_img = np.array(Image.open("test.png"))
# im = plt.imread("background.png")
# sh, sw, d = im.shape
#
# figure(figsize=(sw, sh), dpi=600)
# fig, ax = plt.subplots()
# ax = plt.gca()
# ax.set_xlim(0, sw)
# ax.set_ylim(0, sh)
#
# plt.imshow(im, extent=[0, sw, 0, sh])
# plt.text(1500, 1500, "Testdehkjhdedkjegjdgejgdejgdjegdjhegdheghgdegdhegjhdgehgdje", fontsize=4)  # add text
#
# plt.imshow(overlaid_img, extent=[490, 1800, 500, 1800])
#
# plt.axis("off")
# # plt.show()
# plt.savefig("updated_back.png", bbox_inches='tight', dpi=600)

# Import background template

# Plot phase bars
labels = [1] * 400 + [2] * 400 + [3] * 400 + [4] * 400
phase_file = "./reports/case_time_phase.png"
generate_phase_band(labels, file_name=phase_file)

status = [5] * 400 + [6] * 400 + [7] * 400 + [7] * 400
status_file = "./reports/case_time_status.png"
generate_phase_band(status, file_name=status_file)

trainee = [8] * 400 + [9] * 400 + [10] * 400 + [10] * 400
trainee_file = "./reports/case_time_trainee.png"
generate_phase_band(trainee, file_name=trainee_file)

pie_file = "./reports/phase_pie.png"
plot_pie(labels, pie_name=pie_file)

transition_file = "./reports/transition.png"
generate_transition(labels, transition_file)


# combine all infos
im = plt.imread("./src/report_template.png")
sh, sw, d = im.shape
figure(figsize=(sw, sh), dpi=600)
fig, ax = plt.subplots()
ax = plt.gca()
ax.set_xlim(0, sw)
ax.set_ylim(0, sh)
plt.imshow(im, extent=[0, sw, 0, sh])

# Add basic information
phase = Image.open(phase_file)
plt.imshow(phase, extent=[281, 5718, 7206, 7430])

status = Image.open(status_file)
plt.imshow(status, extent=[281, 5718, 6667, 6889])

trainee = Image.open(trainee_file)
plt.imshow(trainee, extent=[281, 5718, 6143, 6362])


# Add durations
counts = get_durations(labels)
locations = [[1416, 5401], [1416, 5166], [1416, 4926], [1416, 4686], [1416, 4440]]
for idx, count in enumerate(counts):
    location = locations[idx]
    plt.text(location[0], location[1], "{:>8d}".format(count), fontsize=4)  # add text

# add proportion
locations = [[2520, 5401], [2520, 5166], [2520, 4926], [2520, 4686]]
total = counts[-1]
for idx, count in enumerate(counts[:-1]):
    location = locations[idx]
    plt.text(location[0], location[1], "{:>2.2f}".format(count / total), fontsize=4)  # add text

# add pie file
pie_duration = Image.open(pie_file)
plt.imshow(pie_duration, extent=[3570, 4740, 4398, 5568])

# add transition
transition = Image.open(transition_file)
plt.imshow(transition, extent=[3730, 5447, 2091, 3566])

# Add scores
score_A =


plt.axis("off")
# plt.show()
case_name = os.path.basename(phase_file).split(".")[0] + "_report"
plt.savefig("./reports/{}.png".format(case_name), bbox_inches='tight', dpi=800, pad_inches=0.0)