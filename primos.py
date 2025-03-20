"""
Nom: Àfrica Abad Trullàs
Modul que defineix funcions amb números primers

>>> esPrimo(4)
False

>>> esPrimo(-2)
True
"""



def esPrimo(numero):
    """"
    esPrimo retorna True si el seu argument es primo, y False si no ho és

    >>> esPrimo(1023)
    False 

    >>> esPrimo(1021)
    True
    """

    for prova in range(2, numero): #range va del primer al últim menys 1
        if numero % prova == 0:
            return False
    
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()



