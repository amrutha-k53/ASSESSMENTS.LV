# -*- coding: utf-8 -*-
"""LVADSUSR143_AMRUTHAK.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t-Bl9swzlwF8lbnOFWa1R6f2w3LOVQIM
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""1.Load Dataset"""

df=pd.read_csv('/content/Final Dataset - IPL.csv')
df.head()

#basic information about dataset
df.info()

"""2.Data Cleaning"""

#check for null values in each column and sum them
df.isnull().sum()
#The data shows there are no null values.If there were any null values use:
#df.dropna()-to drop the null values
#df['col name'].fillna(0)-to fill null values with 0

#check for duplicate values
df.duplicated()
#The data shows no duplicates, if there were duplicates, drop them by
#df.drop_duplicates()

"""3.Descriptive statistics"""

#The mean,standard deviation,count,minimum,maximum,quartiles are all described.
df.describe()

variance=df[['first_ings_score','first_ings_wkts','second_ings_score','second_ings_wkts','margin','highscore']].var()
median=df[['first_ings_score','first_ings_wkts','second_ings_score','second_ings_wkts','margin','highscore']].median()
mode=df[['first_ings_score','first_ings_wkts','second_ings_score','second_ings_wkts','margin','highscore']].mode()

print("Variance is:")
print(variance)

print("\nMedian is:")
print(median)

print("\nMode is:")
print(mode)

"""4.Data Visualization"""

df

# Count the occurrences of each player winning the Player of the Match award
player_potm_counts = df['player_of_the_match'].value_counts()

# Plotting the top players who have won Player of the Match award often
plt.figure(figsize=(10, 6))
player_potm_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top Players Winning "Player of the Match" Award Often')
plt.xlabel('Player')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""5.Identifying relationships"""

#toss decision impact match outcome
sns.scatterplot(x='toss_decision',y='match_winner',data=df)
plt.title("Toss decision impact match outcome")
plt.show()
#The toss decision has an impact on match outcome as most matches are won by the team who won the toss and chose fielding.

"""6.Outlier detection"""

#box plot will help identifying the outliers in the first and second innings wickets.
plt.boxplot(df[['first_ings_wkts','second_ings_wkts']],labels = ['first_ings_wkts','second_ings_wkts'])
#as observed, there seems to be an outlier in the first innings wickets

#Using the inter quartile range, we are bounding the data and removing the outliers
Q1 = df['first_ings_wkts'].quantile(0.25) #first quarter
Q3 = df['first_ings_wkts'].quantile(0.75) #rest 3 quarters
iqr = Q3-Q1
lower_bound = Q1-1.5*iqr
upper_bound = Q3+1.5*iqr
df = df[(df['first_ings_wkts']>lower_bound) & (df['first_ings_wkts']<upper_bound)]

"""7.Performance trends and venue impacts"""

# Calculate team performance metrics
team_performance = df.groupby(['match_winner', 'match_id', 'venue']).agg({
    'second_ings_score': 'sum',
    'second_ings_wkts': 'sum',
}).reset_index()

# Calculate individual performance metrics
individual_performance = df.groupby(['player_of_the_match', 'match_id', 'venue']).agg({
    'second_ings_score': 'sum',
    'second_ings_wkts': 'sum',
}).reset_index()

# Compare performance across matches and venues
# For team performance
team_performance_match_venue_comparison = team_performance.groupby(['match_winner', 'venue']).mean()
# For individual performance
individual_performance_match_venue_comparison = individual_performance.groupby(['player_of_the_match', 'venue']).mean()

# Example output
print("Team Performance across Matches and Venues:")
print(team_performance_match_venue_comparison.head())

print("\nIndividual Performance across Matches and Venues:")
print(individual_performance_match_venue_comparison.head())

"""The venue has an impact on winning the matches for the team Banglore and its best player "Abhishek sharma" who won most matches in "Maharashtra Cricket Association Stadium,Pune "

8.Player spotlight
"""

# Count the occurrences of each player winning the Player of the Match award
player_potm_counts = df['player_of_the_match'].value_counts()

# Calculate the percentage of Player of the Match wins for each player
player_potm_percentage = (player_potm_counts / df.shape[0]) * 100

# Print the top players who have won Player of the Match award often
print("Top players winning Player of the Match award often:")
print(player_potm_percentage.head(10))

# Reasons could include:
# 1. Consistent performance: Players who consistently perform well in matches are more likely to win the award.
# 2. All-round performance: Players who excel in both batting and bowling

"""9."""
