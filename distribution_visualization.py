import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("titanic.csv")


data = data.dropna(subset=["Age"])

# -------- Age Histogram --------
plt.figure(figsize=(8,5))
sns.histplot(data["Age"], bins=20, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.savefig("age_histogram.png")   # 👈 saves image
plt.show()

# -------- Gender Bar Chart --------
gender_count = data["Sex"].value_counts()

plt.figure(figsize=(6,4))
gender_count.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.savefig("gender_barchart.png")   # 👈 saves image
plt.show()
