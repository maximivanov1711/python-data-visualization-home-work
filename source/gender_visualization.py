import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_set = pd.read_csv("./data/StudentsPerformance_prepared.csv")

labels = ["Average math score", "Average reading score", "Average writing score"]
subject_labels = ["math_score", "reading_score", "writing_score"]

male_scores = [
    data_set[data_set["gender"] == 1][s].median() for s in subject_labels
]
female_scores = [
    data_set[data_set["gender"] == 2][s].median() for s in subject_labels
]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, male_scores, width, label="Male", facecolor="#99ccff")
rects2 = ax.bar(x + width / 2, female_scores, width, label="Female", facecolor="#FFC0CB")

ax.set_ylabel("Average score")
ax.set_title("Average scores by gender")
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


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.savefig("./img/gender_visualization.png")
