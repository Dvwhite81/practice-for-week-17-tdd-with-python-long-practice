def parse(arg):
    # if arg == "I":
    #     return 1
    # elif arg == "II":
    #     return 2
    # elif arg == "III":
    #     return 3
    # elif arg == "IV":
    #     return 4
    # elif arg == "V":
    #     return 5
    # elif arg == "VI":
    #     return 6
    # elif arg == "VII":
    #     return 7
    # elif arg == "VIII":
    #     return 8

    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    i = 0
    total = 0
    length = len(arg)

    while i < length:
        if i + 1<length and arg[i:i+2] in roman:
            total+=roman[arg[i:i+2]]
            i += 2
        else:
            total+=roman[arg[i]]
            i += 1
    return total
