nextprime = raw_input("thes na  psaksw ton epomeno prwto arithmo apanta nai/oxi")
arxh = 1


def is_prime(n):
    if n % 2 == 0 :
        return False
    
    for i in range(3, int(n**0.5) + 1, 2) : 
        if n % i == 0 :
            return False

    return True



while nextprime.lower().startswith('n'):
    arxh += 1
    while is_prime(arxh) == False :
        arxh += 1

        print ("o epomenos prwtos einia " + str (arxh))
        nextprime = raw_input("thes na  psaksw ton epomeno prwto arithmo apanta nai/oxi")

        
    
        

