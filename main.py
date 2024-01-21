import pandas as pd
# import Pyarrow

data = pd.read_csv('CMAPSSData/train_FD004.txt', delim_whitespace=True)
print(data.columns)