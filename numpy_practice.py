import numpy as np # everyone alisases it 'np'

a = np.array([1, 2, 3, 4])

print(a + 10)    # [11 12 13 14]  — adds to EVERY element
print(a * 2)     # [2 4 6 8]
print(a ** 2)    # [1 4 9 16]
print(a + a)     # [2 4 6 8]  — element-wise

np.zeros(5)              # [0. 0. 0. 0. 0.]
np.ones(3)               # [1. 1. 1.]
np.arange(0, 10, 2)      # [0 2 4 6 8]  — like range(), but an array
np.linspace(0, 1, 5)     # [0.   0.25 0.5  0.75 1.  ] — 5 evenly spaced points

x = np.linspace(-10, 10, 200)
y = np.sin(x)            # applies sin to all 200 points at once

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)    # (2, 3) — 2 rows, 3 cols
print(a.dtype)    # int64 — the fixed element type
print(a.sum(), a.mean(), a.max())   # 21 3.5 6
print(a[0, 1])    # 2 — row 0, col 1