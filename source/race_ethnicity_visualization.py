import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_set = pd.read_csv("./data/StudentsPerformance_prepared.csv")

labels = ["Average math score", "Average reading score", "Average writing score"]

scores = {}
group_labels = ["group " + l for l in "ABCDE"]
subject_labels = ["math_score", "reading_score", "writing_score"]

for group_label, group_category in zip(group_labels, range(1, len(group_labels) + 1)):
    scores[group_label] = []

    for subject_label in subject_labels:
        scores[group_label].append(
            data_set[data_set["race/ethnicity"] == group_category][subject_label].median()
        )

x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots()
bars = []
for group_label in group_labels:
    bars.append(
        ax.bar(x+width*3, scores[group_label], width, label=group_label)
    )
    x = x + width

ax.set_ylabel("Average score")
ax.set_title("Average scores by race/ethnicity")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='lower right')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate("{}".format(int(height)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha="center", va="bottom")


for bar in bars:
    autolabel(bar)

fig.tight_layout()

plt.savefig("./img/race_ethnicity_visualization.png")
