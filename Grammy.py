import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv(r'C:/Users/asus/Downloads/archive/Grammy Award Nominees and Winners 1958-2024.csv')
df.head()

df.info()
df.describe(include='all')
df.isnull().sum()
df.duplicated().sum()

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

winners = df[df['winner'] == True]
top_artists = winners['nominee'].value_counts().head(10)

top_artists.plot(kind='bar', title='Top 10 Grammy-Winning Artists')
plt.ylabel('Number of Wins')
plt.show()

df['award_name'].value_counts().head(10).plot(kind='bar', title='Most Frequent Categories')
plt.ylabel('Number of Nominations')
plt.show()

df['year'] = pd.to_numeric(df['year'], errors='coerce')
winners_by_year = df[df['winner'] == True]['year'].value_counts().sort_index()

winners_by_year.plot(kind='line', title='Number of Grammy Wins per Year')
plt.xlabel('Year')
plt.ylabel('Total Wins')
plt.show()

df['nominee'].value_counts().head(10).plot(kind='bar', title='Top 10 Most Nominated Artists')
plt.ylabel('Nominations')
plt.show()

top_categories = df['award_name'].value_counts().head(5).index
top_cat_df = df[df['award_name'].isin(top_categories)]

plt.figure(figsize=(12,6))
sns.countplot(data=top_cat_df, x='award_name', hue='winner')
plt.title('Nomination vs Wins in Top Categories')
plt.xticks(rotation=45)
plt.show()

most_nominated = df['nominee'].value_counts().head(10)
most_nominated.plot(kind='bar', title='Top 10 Most Nominated Artists')
plt.ylabel('Nominations')
plt.show()

most_awarded = df[df['winner'] == True]['nominee'].value_counts().head(10)
most_awarded.plot(kind='bar', title='Top 10 Most Awarded Artists')
plt.ylabel('Number of Wins')
plt.show()

nominations = df['nominee'].value_counts()
wins = df[df['winner'] == True]['nominee'].value_counts()

nom_win_df = pd.DataFrame({
    'nominations': nominations,
    'wins': wins
}).fillna(0)

# Calculate win rate
nom_win_df['win_rate'] = nom_win_df['wins'] / nom_win_df['nominations']
top_win_rate = nom_win_df[nom_win_df['nominations'] >= 5].sort_values('win_rate', ascending=False).head(10)

top_win_rate[['win_rate']].plot(kind='barh', legend=False, title='Top Win Rate Artists (≥5 Nominations)')
plt.xlabel('Win Rate')
plt.show()

