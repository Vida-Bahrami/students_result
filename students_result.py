import pandas as pd

df_student = pd.read_csv('students_score.csv')
print(df_student.head())
subjects = ['math', 'physics','chemistry', 'biology', 'english']
df_student['best_subject'] = df_student[subjects].idxmax(axis=1)
df_student['worst_subject'] = df_student[subjects].idxmin(axis=1)
df_student['average'] = df_student[subjects].mean(axis=1)
print(df_student.head())