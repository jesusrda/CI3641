# zipWith implementation
def zipWith(a, b, f):
    if a and b:
        yield f(a[0], b[0])
        for p in zipWith(a[1:], b[1:],f):
            yield p