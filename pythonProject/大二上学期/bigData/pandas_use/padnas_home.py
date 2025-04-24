import pandas as pd
import numpy as np

# 1.
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'e'])
# 2.
s1_res1 = s1 + 5
s1_res2 = s1 - 5
print(s1_res1, s1_res2)
# 3.
s2_res1 = s2 + 10
s2_res2 = s2 - 10
s2_res3 = s2 * 10
print(s2_res1, s2_res2, s2_res3)
# 4.
math_res1 = s2 + s1
math_res2 = s2 - s1
math_res3 = s2 * s1
math_res4 = s2 / s1
print(math_res1, math_res2, math_res3, math_res4)
# 5.
s1_in_res1 = 'a' in s1
s1_in_res2 = 's' in s1
s1_in_res3 = 'c' in s1
print(s1_in_res1, s1_in_res2, s1_in_res3)
# 6.
s2_in_res1 = 'q' in s2
s2_in_res2 = 'w' in s2
s2_in_res3 = 'c' in s2
print(s2_in_res1, s2_in_res2, s2_in_res3)
# 7
add_s1_s2 = s1 + s2
print(add_s1_s2)
# 8.
sub_s1_s2 = s2 - s2
print(sub_s1_s2)
# 9.
s1.index = ['z', 'x', 'c', 'v']
print(s1)
# 10.
s2.index = ['z', 'x', 'c', 'v']
print(s2)
# 11.
arr = pd.Series([1, 2, np.nan, 4, 5])
arr1 = pd.Series([np.nan, 20, 30, 40, 50])
# 12.
arr_res1 = arr1 + arr
arr_res2 = arr1 - arr
arr_res3 = arr1 * arr
arr_res4 = arr1 / arr
print(arr_res1, arr_res2, arr_res3, arr_res4)
