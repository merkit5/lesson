'''jjj'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']=(12,5)
df = pd.read_csv("Pakistan Intellectual Capital - Computer Science - Ver 1.csv",
                 encoding = "ISO-8859-1")
print(df)

sns.set_style('whitegrid')
plt.subplots(figsize=(15,10))
sns.countplot(y="Department", data=df)
plt.title('Количество преподавателей по направлениям', fontsize=18)
plt.show()

plt.subplots(figsize=(12,10))
sns.set_style('whitegrid')
sns.countplot(y="Country", data=df)
plt.xlabel("Количество преподавателей", fontsize=18)
plt.ylabel("Название страны", fontsize=18)
plt.title("Количество преподавателей из разных стран", fontsize=22)
plt.tick_params(labelsize=15)
plt.show()
