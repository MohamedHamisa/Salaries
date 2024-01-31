import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('Salaries.csv')
df.head()

df.columns

df.info()
df.shape
df.isnull().sum()
df.describe()
df['TotalPayBenefits'].mean()

df['TotalPayBenefits'].mean()
df['TotalPayBenefits'].median()
df['TotalPayBenefits'].mode()
df['TotalPayBenefits'].min()
df['TotalPayBenefits'].max()
df['TotalPayBenefits'].max() - df['TotalPayBenefits'].min()
df['TotalPayBenefits'].std()

# why did you fill the missing values with mean?
# Because the mean is the average of the numbers due to mean is a central tendency of data.
df['BasePay'].fillna(df['BasePay'].mean(), inplace=True)
df['OvertimePay'].fillna(df['OvertimePay'].mean(), inplace=True)
df['OtherPay'].fillna(df['OtherPay'].mean(), inplace=True)
df['Benefits'].fillna(df['Benefits'].mean(), inplace=True)
df['Notes'].fillna(df['Notes'].mean(), inplace=True)
df.isnull().sum()

# histogram
df['TotalPayBenefits'].hist()

# bar chart
df['TotalPayBenefits'].value_counts().plot(kind='bar')

# pie chart
df['Year'].value_counts().plot(kind='pie')

df.groupby('Year')['TotalPayBenefits'].describe()
df.groupby('Year')['TotalPayBenefits'].mean()
df.groupby('JobTitle')['TotalPayBenefits'].mean()

# correlation between salary and another numerical column
df.plot.scatter(x='TotalPayBenefits', y='BasePay')

df.plot.scatter(x='TotalPayBenefits', y='OvertimePay')

df.plot.scatter(x='TotalPayBenefits', y='OtherPay')

df.plot.scatter(x='TotalPayBenefits', y='Benefits')

df.plot.scatter(x='TotalPayBenefits', y='Year')
