import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('s.csv', engine='python')
age = df["age"].fillna(22)
df["income"] = df["income"].str.replace(",", "")
income = df["income"].fillna(20000)
income = income.astype(float)
gender = df["gender"]
race = df["race_o"]
attractive_importance = df["attr1_1"]
print(df["attr1_1"].describe())
df["gender"]= df["gender"].map({
0: "Female",
1:"Male"
})
print(df["attr1_1"])
print(df.groupby("gender")["attr1_1"].mean())

sum = 0
sum2 = 0
#female = 0
#male = 1
female_list = []
male_list = []


# for i in age:
#   sum += i
#   print(i)
# print(sum)
# average = sum/len(age)
# print(average)



# v = 0
# for j in income:
#   sum2 += j
#   v = j
#   print(v)
# print(sum2)
# average = sum2/len(income)
# variance = (v-average)**2/len(income)
# print("Average",average)
# print("Variance" , variance)


# df["race_o"]= df["race_o"].map({1:"black",
#  2:"european_caucasian",
#  3:"latino_hispanic_american",
#  4:"asian_pi_asian_american",
#  5:"native_american",
#  6: "other" })


# race_counts=df.race_o.value_counts()
# race_counts.plot.bar()
# print("b_count =", b_count)
# print("ec_count =", ec_count)
# print("lha_count =", lha_count)
# print("apaa_count =", apaa_count)
# print("na_count =", na_count)
# print("other_count =", other_count)

