def our_gen(x):
    for i in range(x+1):
        yield i

gen = our_gen(12)
gen
list(gen)
next(gen)
