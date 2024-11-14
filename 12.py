import pandas as pd
import numpy as np

np.random.seed(24)
df = pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))
print(df)
