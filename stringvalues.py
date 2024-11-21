
series = pd.Series(['  hello  ', ' world ', ' python  ', ' pandas'])
print("Original Series:")
print(series)

print("\nWithout white spaces:")
print(series.str.strip())

print("\nWithout left-sided white spaces:")
print(series.str.lstrip())

print("\nWithout right-sided white spaces:")
print(series.str.rstrip())

