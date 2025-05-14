

def squareRoot(x):
    return squareRootGuess(x, 1)

def squareRootGuess(x, g):
    if abs(x - (g ** 2)) < 0.0001:
        return g

    return squareRootGuess(x, (g + (x/g)) / 2)

def assertAlmostEqual(x, root, decimals):
    if abs(x - root) < 1 / (10 ** decimals):
        return True
    else:
        return False

# test cases
four_root = squareRoot(4)
nine_root = squareRoot(9)
sixteen_root = squareRoot(16)
twentyfive_root = squareRoot(25)
thirtysix_root = squareRoot(36)


print(assertAlmostEqual(four_root, 2, 4))
print(assertAlmostEqual(nine_root, 3, 4))
print(assertAlmostEqual(sixteen_root, 4, 4))
print(assertAlmostEqual(twentyfive_root, 5, 4))
print(assertAlmostEqual(thirtysix_root, 6, 4))






