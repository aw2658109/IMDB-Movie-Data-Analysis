import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("IMDB_Movie.csv")
print(df)
#Q:1 DISPLAY TOP 10 ROWS OF THE DATASET:
print(df.head(10))

# Q:2: CHACK LAST 10 ROWS OF THE DATASETS:
print(df.tail(10))

#Q:3: FIND SHAPE OF OUR DATASET (NUMBER OF ROWS AND COLUMNS):
print(np.shape(df))
print("NUMBER OF ROWS:",df.shape[0])
print("NUMBER OF COLUMNS:",df.shape[1])

#Q:4: GETTING INFORMATION ABOUT OUR DATASET LIKE TOTAL NUMBER OF ROW AND TOTAL  NUMBER OF COLUMNS:
# DATATYPE OF EACH OF COLUMNS AND MEMORY REQUIRMENTS:
print(df.info())

#Q:5: CHECK MISSING VALUES IN DATASET:
print("Any missing value:",df.isnull().values.any())

print(df.isnull().sum())
# HEATMAP FOR NULL VALUES:
plt.figure(figsize=(6,6))
sns.heatmap(df.isnull())
plt.show()
# PERCENTAGE FO MISSING VALUE:
per_missing=df.isnull().sum()*100/len(df)
print(per_missing)

#Q: 6: DROP THE ALL MISSING VALUE IN OUR DATASETS:
df.dropna(axis=0, inplace=True)
print(df)

#Q: 7: CHECK FOR DUPLICATE DATA:
dup=df.duplicated().any()
print("Any duplicated values:",dup)
print(df.drop_duplicates())

#Q:8: GET OVERALL STATISTICS ABOUT THE DATA FRAME:
print(df.describe())


#Q:8: GET OVERALL STATISTICS ABOUT THE DATA FRAME:
print(df.describe(include="all"))

#Q:9:DISPLAY TITLE OF THE  MOVIE HAVING RUNTIME=>180 MINUTES:
print(df.columns)

#Q:9:DISPLAY TITLE OF THE  MOVIE HAVING RUNTIME=>180 MINUTES:
data=df[df['Runtime (Minutes)']>=180]['Title']
print(data)

#Q:10: IN WHICH YEAR THERE WAS THE HIGHEST AVERAGE VOTING:
data1=df.groupby("Year")["Votes"].mean().sort_values(ascending=False)
print(data1)

#BARPLOT:
sns.barplot(x="Year",y="Votes",data=df)

plt.title("Voting By Year")
plt.show()

#Q:11: IN WHICH YEAR THERE WAS THE HIGHEST AVERAGE Revenue:
data2=df.groupby("Year")['Revenue (Millions)'].mean().sort_values(ascending=False)
print(data2)
#BARPLOT:
sns.barplot(x="Year",y='Revenue (Millions)',data=df)
plt.title("Revenue (Millions) By Year")
plt.show()

#Q:12: FIND THE AVERAGE RATING OF THE EACH DIRECTOR:
data3=df.groupby("Director")["Rating"].mean().sort_values(ascending=False)
print(data3)

#Q:13:DISPLAY TOP 10 LENGTHY MOVIES TITLE AND RUNTIME:
data4=df.nlargest(10,'Runtime (Minutes)')[["Title",'Runtime (Minutes)']].set_index("Title")
print(data4)

# BARPLOT:
plt.figure(figsize=(10,10))
sns.barplot(x="Runtime (Minutes)",y=data4.index,data=data4)
plt.title("Title By Runtime (Minutes)",fontsize=20)
plt.show()


#Q:14: DISPLAY NUMBER OF MOVIE PER YEAR:
data5=df["Year"].value_counts()
print(data5)
sns.countplot(x="Year",data=df)
plt.title("Number of Movie Per Year",fontsize=20)
plt.show()

#Q:15: FIND THE MOST POPULAR MOVIE TITLE (HIGHEST REVENUE):
data6=df[df["Revenue (Millions)"].max()==df["Revenue (Millions)"]]["Title"]
print(data6)

#Q:16: DISPLAY TOP 10 HIGHEST RATED  MOVIE TITLES AND ITS DIRECTORS:
data7=df.nlargest(10,"Rating")[['Title','Rating','Director']].set_index('Title')
print(data7)

sns.barplot(x="Rating",y=data7.index, data=data7,hue='Director')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()

#Q:17: DISPLAY TOP 10 HIGHEST REVENUE OF MOVIE TITLE:
data8=df.nlargest(10,"Revenue (Millions)")[['Title',"Revenue (Millions)"]].set_index('Title')
print(data8)

sns.barplot(x="Revenue (Millions)",y=data8.index, data=data8)
plt.show()

#Q:18: FIND THE AVERAGE RATING OF MOVIES YEAR WISE:
data9=df.groupby("Year")["Rating"].mean().sort_values(ascending=False)
print(data9)

#Q:19: DOES RATING AFFECT THE REVENUE:

sns.scatterplot(x="Rating", y="Revenue (Millions)", data=df)
plt.show()

#Q:20: CLASSIFY MOVIE BASED ON RATING [EXCELLENT,GOOD AND AVERAGE]:
# Define the function with the correct syntax
def cate_rating(rating):
    if rating >= 7.0:
        return "Excellent"
    elif rating >= 6.0:
        return "Good"
    else:
        return "Average"
df["rating_cat"] = df['Rating'].apply(cate_rating)
print(df)

#Q:21:COUNT NUMBER OF ACTION MOVIES:
data10=len(df[df["Genre"].str.contains("action",case=False)])
print(data10)

#Q:22:FIND UNIQUE VALUE FROM GENRE:
genre_uniq=df["Genre"].unique()
print(genre_uniq)

#Q:23: HOW MANY FILMS OF EACH GENRE WERE MADE:
genre_counts = df['Genre'].value_counts()
print(genre_counts)