import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_set = pd.read_csv("../data/StudentsPerformance_prepared.csv")

labels = ["Average math score", "Average reading score", "Average writing score"]

scores = {}
preparation_test = ["None", "Completed"]
subject_labels = ["math_score", "reading_score", "writing_score"]

for test, test_category in zip(preparation_test, range(2)):
    scores[test] = []

    for subject_label in subject_labels:
        scores[test].append(
            data_set[data_set["preparation_course"] == test_category][subject_label].median()
        )

x = np.arange(len(labels))
width = 0.3

fig, ax = plt.subplots()
bars = []
for test in preparation_test:
    bars.append(
        ax.bar(x+width*1.5, scores[test], width, label=test)
    )
    x = x + width

ax.set_ylabel("Average score")
ax.set_title("Average scores by test preparation course")
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

plt.savefig("../img/preparation_course_visualization.png")
