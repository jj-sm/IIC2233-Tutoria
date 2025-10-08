def acumulador():
    total = 0
    while True:
        n = yield total
        if n is not None:
            total += n
        if n is None:
	        total += 2

gen = acumulador()
print(next(gen))
print(gen.send(10))
print(gen.send(5))
print(gen.send(7))
print('\n')
print(next(gen))
print(next(gen))