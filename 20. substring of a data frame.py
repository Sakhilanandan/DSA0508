import pandas as pd
data = {
    'Text': ['apple', 'banana', 'orange', 'grape', 'pineapple']
}
df = pd.DataFrame(data)
substring = 'apple'
indexes = df[df['Text'].str.contains(substring)].index
print("Indexes of rows containing the substring '{}':".format(substring))
print(indexes)
