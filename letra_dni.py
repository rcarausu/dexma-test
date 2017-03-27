def calc_letra(nums):
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', \
              'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'L', 'C', 'K', 'E']

    return letras[nums % 23]

l = calc_letra(54655567)
print(l)