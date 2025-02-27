import pandas as pd


sales_data = {
    'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone', 'Television', 'Home Theater',
             'Television', 'Television', 'Television', 'Home Theater', 'Television', 'Home Theater',
             'Home Theater', 'Television', 'Video Games', 'Home Theater', 'Cell Phone'],
    'OrderDate': ['1-6-18', '1-23-18', '2-9-18', '2-26-18', '3-15-18', '4-1-18', '4-18-18', '5-5-18',
                  '5-22-18', '6-8-18', '6-25-18', '7-12-18', '7-29-18', '8-15-18', '9-1-18', '9-18-18',
                  '10-5-18', '10-22-18'],
    'Region': ['East', 'Central', 'Central', 'Central', 'West', 'East', 'Central', 'Central', 'West', 'East',
               'Central', 'East', 'East', 'Central', 'East', 'Central', 'East', 'Central'],
    'Manager': ['Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy', 'Martha', 'Hermann', 'Hermann', 'Douglas',
                'Martha', 'Hermann', 'Martha', 'Douglas', 'Martha', 'Hermann', 'Martha', 'Douglas', 'Martha'],
    'SalesMan': ['Alexander', 'Shelli', 'Luis', 'David', 'Stephen', 'Alexander', 'Luis', 'Sigal', 'Michael',
                 'Alexander', 'Sigal', 'Diana', 'Karen', 'Alexander', 'Sigal', 'Alexander', 'John', 'Alexander'],
    'Units': [95, 50, 36, 27, 56, 60, 75, 90, 32, 60, 90, 29, 81, 35, 2, 16, 28, 64],
    'Unit_price': [1198.00, 500.00, 1198.00, 225.00, 1198.00, 500.00, 1198.00, 1198.00, 1198.00, 500.00, 1198.00,
                    500.00, 500.00, 1198.00, 58.50, 500.00, 500.00, 225.00],
    'Sale_amt': [113810.00, 25000.00, 43128.00, 6075.00, 67088.00, 30000.00, 89850.00, 107820.00, 38336.00,
                  30000.00, 107820.00, 14500.00, 40500.00, 41930.00, 250.00, 936.00, 14000.00, 14400.00]
}
sales_df = pd.DataFrame(sales_data)
sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'])
pivot_table = sales_df.pivot_table(index=['Region', 'Manager', 'SalesMan'], values='Sale_amt', aggfunc='sum')
print("Pivot Table for Total Sale Amount:")
print(pivot_table)
