import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=pd.read_csv('Student Social media Addiction.csv')

#barplot
#Barplot is for showing categorical data vs numeric data.
sns.barplot(x='Gender', y='Avg_Daily_Usage_Hours', data=data,errorbar=None,estimator=np.sum,palette='pastel',order=['Male','Female'])

'''What is an estimator?
In Seaborn, when you make plots like barplot or pointplot, you often have multiple values for each category. The estimator is a function that tells Seaborn how to summarize those multiple values into a single value per category.Default estimator = np.mean → it calculates the average.You can change it to sum, median, min, max, custom function, whatever you want.
'''

#horizontal barplot
sns.barplot(y='Gender',x='Avg_Daily_Usage_Hours',data=data,errorbar=None)

#Countplot (Frequency of Categories)
sns.countplot(x='Gender',data=data,palette='Set2')

#Scatterplot (Two Numeric Columns)
sns.scatterplot(x='Age',y='Sleep_Hours_Per_Night',data=data, hue='Gender',style='Gender')


#Boxplot (Distribution & Outliers)
#Shows median, quartiles, and outliers in usage hours
sns.boxplot(x='Gender', y='Avg_Daily_Usage_Hours', data=data, palette='coolwarm')

#pointplot
sns.pointplot(x='Gender', y='Avg_Daily_Usage_Hours', data=data)


#Heatmap (Correlation)
data = pd.DataFrame({
    'Math': [90, 80, 70],
    'English': [85, 88, 78],
    'Science': [92, 77, 85]
}, index=['Alice','Bob','Charlie'])

corr = data.corr()  # numeric columns only
sns.heatmap(corr, annot=True, cmap='Blues')


