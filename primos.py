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


def primos(numero):
    """
    retorno una tupla amb tots els num primos menors que el seu argument
    """
    res = []
    for prova in range(2, numero):
        if esPrimo(prova) == True:
            res.append(prova)

    return tuple(res)


def descompon(numero):
    """
    Retorna una tupla amb la descomposició en factors primers del seu argument 
    """
    factors = [] 
    divisor = 2
    while numero > 1:

        if numero % divisor == 0:
            numero = numero//divisor 
            factores.append(divisor)
            divisor = 2
        else:
            divisor += 1

    return tuple(factors) 


def mcd(numero1, numero2):
    #se multiplican factores comunes
    n1 = descompon(numero1)
    n2 = descompon(numero2)
    n1 = set(n1) #convertimos a conjunto (no repetidos)
    n2 = set(n2)
    res = 1
    for prova in n1:
        if prova in n2:
            res = res*prova
            
    return res


def mcm(numero1, numero2):
    #formula de mcd a mcm
    return (numero1 * numero2) // mcd(numero1, numero2)


def mcdN(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultat = mcd(resultat, num)
        
    return resultat


def mcmN(*numeros):    
    resultat = numeros[0]
    for num in numeros[1:]:
        resultat = mcm(resultat, num)
        
    return resultat


if __name__ == "__main__":
    import doctest
    doctest.testmod()