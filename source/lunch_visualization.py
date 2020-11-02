import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_set = pd.read_csv("../data/StudentsPerformance_prepared.csv")

labels = ["Average math score", "Average reading score", "Average writing score"]

scores = {}
lunch_types = ["Standard", "Free/reduced"]
subject_labels = ["math_score", "reading_score", "writing_score"]

for lunch, lunch_category in zip(lunch_types, range(1, len(lunch_types) + 1)):
    scores[lunch] = []

    for subject_label in subject_labels:
        scores[lunch].append(
            data_set[data_set["lunch"] == lunch_category][subject_label].median()
        )

x = np.arange(len(labels))
width = 0.3

fig, ax = plt.subplots()
bars = []
for lunch in lunch_types:
    bars.append(
        ax.bar(x+width*1.5, scores[lunch], width, label=lunch)
    )
    x = x + width

ax.set_ylabel("Average score")
ax.set_title("Average scores by lunch type")
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

plt.savefig("../img/lunch_visualization.png")
