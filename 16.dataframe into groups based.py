import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Jane', 'Mike'],
    'Age': [15, 17, 16, 15, 18],
    'School_Code': ['S001', 'S002', 'S001', 'S003', 'S002']
}
df = pd.DataFrame(data)


grouped = df.groupby('School_Code')

print(type(grouped))
