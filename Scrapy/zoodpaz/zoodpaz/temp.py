a='000010'
b='010101'

def compare_bits(A, B):
    c_1 = str(int(A) & int(B))
    c = (len(A) - len(c_1))*'0' + str(c_1)
    return c

q = compare_bits(a, b)
if("1" in q):
    print("ready")
