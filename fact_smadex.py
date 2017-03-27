def fact(max):
    n = 1

    if n == 1:
        return n
    else:
        return fact(n-1)*n

def check_larger_fact(n):
    i = 0
    while fact(i) < n:
         i += 1

    print(fact(i), i)

check_larger_fact(10)