
import numpy as np

exam_data = {
    'name': ['RISHABH KUMAR', 'SATYAM SINGH', 'SAURABH MISHRA', 'SHAURYA SHAKYA', 'SHIVAM'],
    'score': [12.5, 9, 16.5, np.nan, 9],
    'attempts': [1, 3, 2, 3, 2],
    'qualify': ['yes', 'no', 'yes', 'no', 'no']
}
labels = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame(exam_data, index=labels)
print("DataFrame:")
print(df)

