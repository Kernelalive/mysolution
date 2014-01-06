

def fibo ( n ):
    a = 0
    b = 1
    while b <= n:
        print b
        c = a
        a = b
        b = c + b
        
    

x = raw_input('vale posa psifia apo thn akolouthia fibo thes na ypologisw ')
fibo(int(x))
