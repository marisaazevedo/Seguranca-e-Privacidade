import random

def isMillerRabinPassed(number):
    # Encontra o maior valor de divisões por dois
    maxDivisionsByTwo = 0
    ec = number - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2 ** maxDivisionsByTwo * ec == number - 1)

    def trialComposite(round_tester):
        # Verifica se o número é composto por meio do teste de Miller-Rabin
        if pow(round_tester, ec, number) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * ec, number) == number - 1:
                return False
        return True

    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, number)
        if trialComposite(round_tester):
            return False
    return True

def nextPrime(N):
    if N <= 1:
        return 2

    prime = N
    found = False

    while not found:
        prime += 1

        if isMillerRabinPassed(prime):
            found = True

    return prime
