import pandas as pd
data = {
    'Name': ['John', 'Alice', 'Bob', 'Jane', 'Mike'],
    'Age': [15, 17, 16, 15, 18],
    'School_Code': ['S001', 'S002', 'S001', 'S003', 'S002'],
    'Class': ['A', 'B', 'A', 'B', 'A']
}
df = pd.DataFrame(data)
grouped = df.groupby(['School_Code', 'Class'])
for group_name, group_df in grouped:
    print(f"Group: {group_name}")
    print(group_df)
    print()
