import pandas as pd
from colorama import init, Fore, Back

data_set = pd.read_csv("StudentsPerformance.csv")

data_set["gender"] = data_set["gender"].map({
    "male": 1,
    "female": 2
})

data_set["race/ethnicity"] = data_set["race/ethnicity"].map({
    "group A": 1,
    "group B": 2,
    "group C": 3,
    "group D": 4,
    "group E": 5
})

data_set["education"] = data_set["parental level of education"].map({
    "some high school": 1,
    "high school": 2,
    "some college": 3,
    "bachelor's degree": 4,
    "associate's degree": 5,
    "master's degree": 6
})
data_set.drop(["parental level of education"], axis=1, inplace=True)

data_set["lunch"] = data_set["lunch"].map({
    "standard": 1,
    "free/reduced": 2
})

data_set["preparation_course"] = (data_set["test preparation course"] == "completed").astype("int")
data_set.drop(["test preparation course"], axis=1, inplace=True)

data_set.rename(columns={
    "math score": "math_score",
    "reading score": "reading_score",
    "writing score": "writing_score"
}, inplace=True)
data_set = data_set.reindex(columns=[
    "gender",
    "race/ethnicity",
    "education",
    "lunch",
    "preparation_course",
    "math_score",
    "reading_score",
    "writing_score"
])

init(autoreset=True)
if len(data_set) == len(data_set.dropna()):
    print(Fore.BLACK + Back.GREEN + 'Обработка данных успешно завершена...')

    data_set.to_csv("StudentsPerformance_prepared.csv")
else:
    print(Fore.BLACK + Back.RED + 'При обработке данных произошла ошибка!')
