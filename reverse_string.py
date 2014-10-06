def reverse_string(abc):
    abc = list(abc);
    reverse_abc = [];
    for i in range(0, len(abc)):
        reverse_abc.append(abc.pop())
    print ("the reverse string is " + str(reverse_abc))



    

def main():
    eisodos = raw_input("Enter a string you wanna reverse\n")
    reverse_string(eisodos)


    
if __name__ == "__main__":
    main()
