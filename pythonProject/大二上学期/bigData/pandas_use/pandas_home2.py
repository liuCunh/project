import pandas as pd
import numpy as np

# 1.
data = [['tom', 'male', 90], ['Jerry', "male", 89], ['Lily', 'female', 98]]
df = pd.DataFrame(data, columns=['name', 'sex', 'score'])

# 2.
df.index = ['one', 'two', 'three']
print(df)

# 3.
res = 'score' in df

# 4.
res1 = 'three' in df.index

# 5.
res2 = 'two' in df.index

# 6.
data_arr = [np.array(('tom', 'male', 90)), np.array(('Jerry', 'male', 89)), np.array(("Lily", 'female', 98))]
np_df = pd.DataFrame(data_arr, index=['one', 'two', 'three'], columns=['name', 'sex', 'score'])
print(np_df)

# 7.
np_res = np_df.shape
print(np_res)
for i in np_df.values:
    print(i, end=", ")
