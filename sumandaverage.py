
numbers = []
while True:
    num = int(input("Enter a number (0 to finish): "))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}, Average: {average}")
else:
    print("No numbers entered.")

