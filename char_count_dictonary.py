from lzma import PRESET_DEFAULT


def count_char(s):
    """"Fucntion to count repeated caracter on a string
    E.g.:
    >>> count('willian')
    {'a' : 1, i : 2, l : 1, n : 1, w :1,}
    >>> count('banana')
   {'a' : 3,'b' : 1,'n' : 2,}
    
    
    :param s: string to be counted
    
    """
    
    sorted_caracters = sorted(s)
    preview_caracter = sorted_caracters[0]
    count = 1
    result = {}
    for caracter in sorted_caracters[1:]:
        if caracter == preview_caracter:
            count += 1
        else:
            result[caracter] = count
            preview_caracter = caracter
            count = 1
    result[preview_caracter] = count
    return result
if __name__ == '__main__':
    
    print(count_char('willian'))
    
    print(count_char('banana'))
    ##
    