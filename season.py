
def find_season(month, day):
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 21):
        return "Winter"
    elif (month == 3 and day >= 21) or (4 <= month <= 5) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 21):
        return "Summer"
    else:
        return "Autumn"

month = 7
day = 15
print(f"The season for {month}/{day} is {find_season(month, day)}.")

