import matplotlib.pyplot as plt
import numpy as np

models = ("ResNet50", "ResNet152", "VGG16", "VGG19", "InceptionResNetV2", "InceptionV3", "EfficientNetB7")

# Accuracy Values - set y_lim to 1.1
values = {
    'Training': (0.9843, 0.9902, 1,0.9961,1,0.9941,0.815),
    'Validation': (0.95,0.9312,0.975,0.9625,0.9375,0.9625,0.8687),
    'Test': (0.9333,0.9556,0.9778,0.9833,0.95,0.9556,0.9),
}

# Loss Values - set y_lim to 2
# values = {
#     'Training': (0.0504, 0.0214, 0.013,0.0189,0.0018,0.0878,1.9407),
#     'Validation': (0.2464,0.5332,0.084,0.1609,0.8609,0.8078,1.46),
#     'Test': (0.037,0.251,0.0007,0.0584,0.5152,0.7297,0.8036),
# }

# Time Values (Time per image)
# values = {
#     'Training & Validation': (0.291481481, 0.7744444,0.86777778,0.996296296,0.442962963,0.1755555,0.875185185),
#     'Test': (0.216667,0.511111,0.627777,0.761111,0.27777,0.133333,0.616666),
# }

x = np.arange(len(models))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='tight')
bar_colours = ["darkorange","indianred","deepskyblue"]
#bar_colours = ["indianred","deepskyblue"]
i=0

for attribute, measurement in values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, color=bar_colours[i])
    #ax.bar_label(rects, padding=3)
    multiplier += 1
    i += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Accuracy')
ax.set_xlabel('Transfer Learning Model')
ax.set_xticks(x + width, models)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 1.1)
plt.tick_params(axis='x', which='major', labelsize=6)

plt.show()