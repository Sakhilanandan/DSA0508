import pandas as pd

np.random.seed(0)
data = {
    'Item': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Sale_Value': np.random.randint(100, 1000, size=6),
    'Units_Sold': np.random.randint(10, 100, size=6)
}

sales_df = pd.DataFrame(data)

pivot_max_min_sale = sales_df.pivot_table(index='Item', values='Sale_Value', aggfunc={'Sale_Value': [max, min]})
print("Pivot Table for Maximum and Minimum Sale Value:")
print(pivot_max_min_sale)

pivot_unit_sold = sales_df.pivot_table(index='Item', values='Units_Sold', aggfunc='sum')
print("\nPivot Table for Item-wise Unit Sold:")
print(pivot_unit_sold)
