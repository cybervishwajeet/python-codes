import numpy as np
import pandas as p
# Numpy functions


# Pandas functions
  # Generate descriptive statistics of the DataFrame
arr = np.array([4,5,57,8,4])
print("The array is:",arr)
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
print("Mean:",mean)
print("Median:",median)
print("Standard Deviation",std_dev)
obj1 = {'Name':['Vedant','Mayuri','Vedant','Mayuri'],
        'age':[18,18,18,18],
        'city':['Pune','Pune','Pune','Pune']}
dp = p.DataFrame(obj1)
dp.head(2)  # Display the first few rows of the DataFrame
dp.tail(1)  # Display the last few rows of the DataFrame
dp.info()  # Display information about the DataFrame
dp.describe()
print("\nPandas DataFrame:")
print(dp)