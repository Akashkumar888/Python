
def zodiac_sign(day, month):
    signs = [
        (20, "Capricorn"), (19, "Aquarius"), (20, "Pisces"),
        (20, "Aries"), (21, "Taurus"), (21, "Gemini"),
        (22, "Cancer"), (22, "Leo"), (22, "Virgo"),
        (23, "Libra"), (22, "Scorpio"), (21, "Sagittarius")
    ]
    return signs[month - 1][1] if day > signs[month - 1][0] else signs[month - 2][1]

day, month = 15, 7
print(f"The astrological sign for {day}/{month} is {zodiac_sign(day, month)}.")

