
data = {
    'col1': [1, 4, 3, 4, 5],
    'col2': [4, 5, 6, 7, 8],
    'col3': [7, 8, 9, 0, 1]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

selected_rows = df[df['col1'] == 4]
print("\nRows where col1 value is 4:")
print(selected_rows)

