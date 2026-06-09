import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Exercitiul 1
df = pd.read_csv('data.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)


# Exercitiul 2
jucatori_varsta = df[df['Age'] > 40].head(10)
print(jucatori_varsta)


# Exercitiul 3
jucatori_top = df[(df['Overall'] >= 85) & (df['Age'] < 25)]
print(jucatori_top)


# Exercitiul 4
sortati = df.sort_values(by='Skill Moves', ascending=False)
print(sortati[['Name', 'Skill Moves']].head(20))


# Exercitiul 5
contract_2021 = df[df['Contract Valid Until'] == '2021']
print(contract_2021[['Name', 'Club', 'Contract Valid Until']])


# Exercitiul 6
print(f"Numar de randuri: {df.shape[0]}")
print(f"Numar de coloane: {df.shape[1]}")
print(f"Jucatori unici: {df['Name'].nunique()}")


# Exercitiul 7
top_nationalitati = df['Nationality'].value_counts().head(5)
print(top_nationalitati)


# Exercitiul 8
plt.figure(figsize=(8, 8))
top_nationalitati.plot(kind='pie', autopct='%1.1f%%')
plt.title('Top 5 nationalitati ale jucatorilor')
plt.ylabel('')
plt.show()


# Exercitiul 9
medii = df.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()
print(medii)


# Exercitiul 10
df['Position'] = df['Position'].fillna('Unknown')
print(df['Position'].value_counts())


# Exercitiul 11
medie_pe_club = df.groupby('Club')['Overall'].mean().sort_values(ascending=False)
print(f"Clubul cu cea mai mare medie de Overall: {medie_pe_club.index[0]}")
print(f"Media Overall: {medie_pe_club.iloc[0]:.2f}")


# Exercitiul 12
def converteste_valoare(val):
    if pd.isna(val):
        return 0
    val = str(val).replace('€', '')
    if 'M' in val:
        return float(val.replace('M', '')) * 1000000
    elif 'K' in val:
        return float(val.replace('K', '')) * 1000
    else:
        return float(val) if val else 0

df['Value_num'] = df['Value'].apply(converteste_valoare)
df['Wage_num'] = df['Wage'].apply(converteste_valoare)

cu_valoare_mai_mare = df[df['Value_num'] > df['Wage_num']]
print(f"Jucatori cu valoare > salariu: {len(cu_valoare_mai_mare)}")


# Exercitiul 13
df['is_underpaid'] = df['Wage_num'] < (df['Value_num'] / 100)
print(df[['Name', 'Wage', 'Value', 'is_underpaid']].head(20))


# Exercitiul 14
df['Scor'] = 0.3 * df['Overall'] + 0.3 * df['Potential'] + 0.2 * df['SprintSpeed']
print(df[['Name', 'Overall', 'Potential', 'SprintSpeed', 'Scor']].sort_values(by='Scor', ascending=False).head(10))


# Exercitiul 15
afaceri = df[['Name', 'Wage', 'Value', 'Wage_num', 'Value_num']].copy()
afaceri['difference'] = afaceri['Value_num'] - afaceri['Wage_num']
afaceri = afaceri.sort_values(by='difference', ascending=False)
print(afaceri[['Name', 'Wage', 'Value', 'difference']].head(20))


# Exercitiul 16
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df.head(100), x='Wage_num', y='Value_num', hue='Overall', size='Overall')
plt.xlabel('Salariu')
plt.ylabel('Valoare')
plt.title('Relatia dintre salariu si valoare')
plt.show()


# Exercitiul 17 (Bonus)
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

output_file("jucatori.html")

top_100 = df.head(100)
source = ColumnDataSource(data=dict(
    wage=top_100['Wage_num'],
    value=top_100['Value_num'],
    name=top_100['Name'],
    club=top_100['Club']
))

p = figure(title="Jucatori - Wage vs Value", x_axis_label='Wage', y_axis_label='Value')
p.circle('wage', 'value', size=10, source=source, alpha=0.6)

hover = HoverTool(tooltips=[
    ("Nume", "@name"),
    ("Club", "@club"),
    ("Wage", "@wage"),
    ("Value", "@value")
])
p.add_tools(hover)
show(p)