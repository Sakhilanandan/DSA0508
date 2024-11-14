import pandas as pd
import numpy as np

np.random.seed(0)
data = np.random.randn(10, 4)  # Generating random values
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

df.loc[3:6, 'B'] = np.nan
df.loc[7:9, 'C'] = np.nan

def highlight_nan(val):
    color = 'background-color: yellow' if pd.isna(val) else ''
    return color

styled_df = df.style.apply(highlight_nan)

# Display styled DataFrame
styled_df
