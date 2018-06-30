
CONVERT = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
def get_arabic(roman_number):
    max = 1
    result = 0
    roman_number = roman_number[-1::-1]

    for sign in roman_number:
        if CONVERT[sign] >= max:
            result += CONVERT[sign]
            max = CONVERT[sign]
        else:
            result -= CONVERT[sign]

    if(get_roman(result) == roman_number[-1::-1]):
        return result
    else:
        raise Exception("Недопустимое число")



def get_roman(arabic_number):
    '''Возвращает правильные значения в интервале 1...3999'''
    result = ''
    group = [[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
            ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]]   
    number = int(arabic_number)

    if number < 1 or number > 3999:
        raise Exception("Недопустимое число")

    for i in range(len(group[0])):
        j = 0
        while j < number // group[0][i]:
            result += group[1][i]
            j += 1
        number %= group[0][i]
    return result

ARABIC = set('0123456789')
ROMAN = set('IVXLCDM')
def convert_number(instr):
    try:
        in_set = set(str(instr))
        res = 0
        if (len(in_set) == 0 ):
            res = ''
        elif (in_set <= ARABIC):
            res = get_roman(instr)
        elif(in_set <= ROMAN):
            res = get_arabic(instr)
        else:
            raise Exception("Недопустимые символы")

        return res
    except Exception as e:
        return "Error: " + str(e)