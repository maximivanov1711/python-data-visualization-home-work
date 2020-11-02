import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_set = pd.read_csv("../data/StudentsPerformance_prepared.csv")

labels = ["Average math score", "Average reading score", "Average writing score"]

scores = {}
education_levels = ["Some high school",
                    "High school",
                    "Some college",
                    "Bachelor's degree",
                    "Associate's degree",
                    "Master's degree"]
subject_labels = ["math_score", "reading_score", "writing_score"]

for education, education_category in zip(education_levels, range(1, len(education_levels) + 1)):
    scores[education] = []

    for subject_label in subject_labels:
        scores[education].append(
            data_set[data_set["education"] == education_category][subject_label].median()
        )

x = np.arange(len(labels))
width = 0.13

fig, ax = plt.subplots()
bars = []
for education in education_levels:
    bars.append(
        ax.bar(x + width * 3.5, scores[education], width, label=education)
    )
    x = x + width

ax.set_ylabel("Average score")
ax.set_title("Average scores by parental level of education")
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

plt.savefig("../img/education_visualization.png")
