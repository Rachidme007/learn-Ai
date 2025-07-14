num = "twenty two "
num2 = num.split()
dic = {
    # 1 - 20
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 2,
    # 30 - 39 (skip 31 to 39)
    "thirty": 3,
    # 40 - 49 (skip 41 to 49)
    "forty": 4,
    # 50 - 59 (skip 51 to 59)
    "fifty": 5,
    # 60 - 69 (skip 61 to 69)
    "sixty": 6,
    # 70
    "seventy": 70,
}

print(dic[num2[0]], dic[num2[1]])
