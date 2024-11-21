
import pandas as pd
import numpy as np

# Creating a Series with random numbers
series = pd.Series(np.random.randint(1, 100, 5))
print("Pandas Series:")
print(series)

# Convert to Python list
python_list = series.tolist()
print("\nConverted Python List:", python_list)
print("Type of the list:", type(python_list))

