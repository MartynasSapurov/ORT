#Doc test
def suma(a, b):
    """
    >>> suma(2, 3)
    5
    >>> suma(3, 3)
    6
    >>> suma('A', 'B')
    'AB'
    >>> suma('A', 3)
    Unsupported operation
    >>> suma(45, 1)
    44
    """
    try:
        return a + b
    except:
        print("Unsupported operation")
    return None


def sub(a, b):
    return a -b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Savarankiškai parašykite doc testą sub funkkcija, taip numatykite apsaugą nuo tipų neatitikimo
