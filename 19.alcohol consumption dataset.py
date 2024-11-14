import pandas as pd
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Beer': [10, 20, 15, 25, 30],
    'Wine': [5, 10, 8, 12, 15],
    'Spirits': [8, 12, 10, 15, 20]
}
df = pd.DataFrame(data)
print("Dimensions of the dataset:", df.shape)
print("\nColumn names:")
for column in df.columns:
    print(column)
