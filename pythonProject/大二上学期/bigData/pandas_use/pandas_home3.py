import pandas as pd
import numpy as np

# 1.
data = [[np.random.randint(1, 10) for _ in range(4)] for i in range(4)]
df = pd.DataFrame(data, columns=range(4), index=range(4))
print(df)
# 2.
res1 = df + 10
res2 = df - 10
res3 = df * 10
res4 = df / 10
# 3.
df[4] = [2, 1, 5, 8]
# 4.
df = df.reindex([0, 1, 2, 3, 4])
print("\n", df)
# 5.
df = df.drop(4, axis=0)
df = df.drop(4, axis=1)
print("\n", df)
