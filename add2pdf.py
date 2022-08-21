import numpy as np
from matplotlib.pyplot import figure
from matplotlib import pyplot as plt
from PIL import Image

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
im = plt.imread("./src/background.png")
sh, sw, d = im.shape
figure(figsize=(sw, sh), dpi=600)
fig, ax = plt.subplots()
ax = plt.gca()
ax.set_xlim(0, sw)
ax.set_ylim(0, sh)
plt.imshow(im, extent=[0, sw, 0, sh])

# Add basic information
plt.text(950, 3161, "XXXXX", fontsize=2)  # add text
plt.text(1150, 3161, "XXXXX", fontsize=2)  # add text
plt.text(1350, 3161, "XXXXX", fontsize=2)  # add text

#
overlaid_img = np.array(Image.open("test.png"))
plt.imshow(overlaid_img, extent=[0, 200, 0, 200])

plt.axis("off")
# plt.show()
plt.savefig("updated_back.png", bbox_inches='tight', dpi=800)