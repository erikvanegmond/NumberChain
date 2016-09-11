def numberToString(number, lang='nl'):
    if lang == "nl":
        return number_to_string_nl(number)


numbers = {0:'',
           1: 'een',
           2: 'twee',
           3: 'drie',
           4: 'vier',
           5: 'vijf',
           6: 'zes',
           7: 'zeven',
           8: 'acht',
           9: 'negen',
           10: 'tien',
           11: 'elf',
           12: 'twaalf',
           13: 'dertien',
           14: 'veertien',
           20: 'twintig',
           30: 'dertig',
           40: 'veertig',
           80: 'tachtig',
           100: 'honderd',
           1000: 'duizend',
           1000000: 'miljoen',
           }


def number_to_string_nl(number):
    if number in numbers:
        return numbers[number]
    else:
        string = str(number)
        if len(string) == 2:
            if number < 20:
                return numbers[int(string[1])] + numbers[int(string[0]) * 10]
            else:
                if int(string[0]) * 10 in numbers:
                    tig = numbers[int(string[0]) * 10]
                else:
                    tig = numbers[int(string[0])] + "tig"
                if string[1] == "0":
                    return tig
                return numbers[int(string[1])] + "en" + tig
        elif len(string) == 3:
            if int(string[0]) > 1:
                return numbers[int(string[0])]+numbers[100] + numberToString(int(string[1:]),lang='nl')
            else:
                return numbers[100] + numberToString(int(string[1:]),lang='nl')
        elif len(string) == 4:
            if int(string[1]) != 0:
                if int(string[2:]) > 0:
                    return number_to_string_nl(int(string[:2]))+numbers[100] + number_to_string_nl(int(string[2:]))
                else:
                    return number_to_string_nl(int(string[:2])) + numbers[100]
            else:
                if int(string[0]) > 1:
                    return numbers[int(string[0])] + numbers[1000] + number_to_string_nl(int(string[1:]))
                else:
                    return numbers[1000] + numberToString(int(string[1:]), lang='nl')
        elif len(string) == 5 or len(string) == 6:
            return number_to_string_nl(int(string[:-3]))+numbers[1000]+number_to_string_nl(int(string[-3:]))
        return "unknows"


def chain(number, lang='nl'):
    string = numberToString(number, lang=lang)
    print("{}, ".format(number), end="")
    if number != 4:
        chain(len(string), lang=lang)



for i in range(100,1000000):
    print()
    chain(i)
