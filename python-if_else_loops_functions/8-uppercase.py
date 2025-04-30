#!/usr/bin/python3
def uppercase(str):
    result = ""  # Nəticə saxlamaq üçün boş bir sətir yaradırıq
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Kiçik hərf yoxlamaq
            result += chr(ord(char) - 32)  # Kiçik hərfi böyük hərfə çeviririk
        else:
            result += char  # Əks halda, simvolu olduğu kimi əlavə edirik
    print("{}".format(result))  # Nəticəni çap edirik
