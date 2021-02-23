def suspenso(p):
    for x in p:
        yield x
    acum = []
    for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
        acum += [p]
    for m in suspenso(acum):
        yield m