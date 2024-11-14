import pandas as pd
import numpy as np

np.random.seed(0)
data = np.random.randn(10, 4)  
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

styled_df = df.style.map(color_negative_red)

# Display styled DataFrame
styled_df
