from random import randint

def suma_mentirosa(a, b):
    return a + b + randint(-5, 5)

if __name__ == "__main__":
    print(suma_mentirosa(1, 2))
