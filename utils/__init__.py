__author__ = 'denis'

def singleton(cls):
    def _singleton(*args, **kwarg):
        if _singleton.obj is None:
            _singleton.obj = cls(*args, **kwarg)
        return _singleton.obj
    _singleton.obj = None
    return _singleton


if __name__ == '__main__':
    @singleton
    class A(object):
        def __init__(self, a):
            self.a = a

    @singleton
    class B(object):
        def __init__(self, a):
            self.a = a

    a, b = A(1), A(2)
    print a.a, b.a
    print type(A), type(a)

    c, d = B(3), B(4)
    print c.a, d.a
    print type(B), type(c)

    e = A(5)
    print e.a