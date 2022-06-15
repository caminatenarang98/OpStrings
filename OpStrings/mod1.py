def maxlen(string1,string2):
    if len(string1) > len(string2):
        return print(f"{string1} - {len(string1)}")
    elif len(string1) < len(string2):
        return print(f"{string2} - {len(string2)}")
    else:
        return print("Tamanhos iguais")


def minString(str1, str2):
    if str1 < str2:
        return str1
    elif str2 < str1:
        return str2
    else:
        return print("Tamanhos iguais")