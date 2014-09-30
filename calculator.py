def calculator(op1, op2, praksh):
    if praksh == '+' :
        print (op1 + op2)
        return
    if praksh == '-' :
        print (op1 - op2)
        return
    if praksh == '*' :
        print (op1 * op2)
        return

    if praksh == '/' :
        print (op1 / op2)
        return
    else:
        print ("mh epitrepth praksh try again:)")
        main()
    

def main():
    praksh = raw_input("vale th praksh theleis na kaneis\n")

    op1 = int(raw_input("vale kai ton 1o telesth ths prakshs pou epelekses\n"))

    op2 = int(raw_input("vale ton 2o telesth\n"))

    calculator(op1, op2, praksh)
    
    
if __name__ == '__main__':
    main()
