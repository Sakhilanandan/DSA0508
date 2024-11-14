import pandas as pd

data = {
    'Text': ['apple', 'Banana', 'Orange', 'grape', 'Pineapple']
}
df = pd.DataFrame(data)

column_to_swap = 'Text'


df[column_to_swap] = df[column_to_swap].str.swapcase()


print("DataFrame after swapping cases:")
print(df)
