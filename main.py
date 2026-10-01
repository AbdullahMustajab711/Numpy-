import numpy as np

scores = np.array([[1,2,3,4,5],
                    [1,1,1,2,4],
                    [3,5,5,7,8]])

print(scores)
print(scores.ndim)   # Number of dimensions
print(scores.shape)  # Rows and columns
print(scores.size)   # Total values
print(scores.dtype)  # Type of values
