import numpy as np
import pandas as pd

# Example using NumPy
arr = np.array([1, 2, 3, 4, 5])
print("NumPy array:", arr)

# Example using Pandas
data = {'Name': ['John', 'Emma', 'Mike', 'Sophia'],
    'Age': [25, 28, 32, 30],
    'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)