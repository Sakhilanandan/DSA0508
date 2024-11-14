import pandas as pd
import numpy as np


data = {
    'A': [1, np.nan, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, np.nan],
    'C': [1, np.nan, 3, np.nan, np.nan]
}
df = pd.DataFrame(data)

df_filtered = df.dropna(thresh=2)

print(df_filtered)
