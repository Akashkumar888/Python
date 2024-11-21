
data = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

col1_series = df['col1']
print("\nFirst column as Series:")
print(col1_series)

