import random




def main():

    flip_times = int(raw_input("enter how many times do you wanna flip a digital coin"))

    head = 0
    tail = 0

    list = ['H', 'T']

    for i in range(flip_times):
        pick = random.choice(list)
        if pick == 'H':
            head += 1
            print ("random pick :Head")
        else:
            tail += 1
            print ("random pick :Tail")

    print("the total number of Heads = " + str(head))
    print("the total number of Tails = " + str(tail))


if __name__ == '__main__':
    main()

    
        
    
