first = [("7", "8", "9")]
second = [("4", "5", "6")]
third = [("1", "2", "3")]
fourth = [("*", "0", "#")]

key_pad = [first, second, third, fourth]

for number in key_pad:
    for num in number:
        print(num, end="")
    print()