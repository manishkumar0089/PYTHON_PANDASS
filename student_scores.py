import pandas as pd
data = {'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','Dana'],
    'Math_Score':[85, 75, 90, 80],
    'Science_Score':[90, 85, 80, 95]}
df = pd.DataFrame(data)
print(df)
import pandas as pd

data = {'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'Dana'],
        'Math_Score': [85, 75, 90, 80],
        'Science_Score': [90, 85, 80, 95]}

df = pd.DataFrame(data)
average_math_score = df['Math_Score'].mean()
print(f"Average Math Score: {average_math_score:.2f}")
highest_science_score = df['Science_Score'].max()
print(f"Highest Science Score: {highest_science_score}")
df['Total_Score'] = df['Math_Score'] + df['Science_Score']
highest_total_score_row = df[df['Total_Score'] == df['Total_Score'].max()]
highest_total_score_name = highest_total_score_row['Name'].values[0]
print(f"Student with the Highest Total Score: {highest_total_score_name}")
average_science_score = df['Science_Score'].mean()
score_difference = average_math_score - average_science_score
print(f"Difference between Average Math and Science Scores: {score_difference:.2f}")
