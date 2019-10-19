import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

# Stack two arrays Vertically
# Method1
np.concatenate([a, b], axis = 0)

# Method2
np.vstack([a, b])

# Method3
np.r_[a, b]

# Stack 2 arrays Horizantally
# Method 1:
np.concatenate([a, b], axis=1)

# Method 2:
np.hstack([a, b])

# Method 3:
np.c_[a, b]
#> array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#>        [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
