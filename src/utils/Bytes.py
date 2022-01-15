class Bytes(object):
    def compare(self, a, b, encoding='utf8'):
        if isinstance(a, bytes):
            a = a.decode(encoding)
        if isinstance(b, bytes):
            b = b.decode(encoding)
        return a == b
