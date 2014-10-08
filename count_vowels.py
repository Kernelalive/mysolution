def isvowel(c):
    vowels = ['a', 'e', 'o', 'i','u']
    for vowel in vowels:
        if c is vowel:
            return True
    return False

def vowel_search(input1):
    sum1 = 0
    vowels_found = []
    for letter in input1:
        if isvowel(letter):
            sum1 += 1
            vowels_found.append(letter)
            

    return (sum1, vowels_found) 
            


def main():
    sentence = raw_input('enter a string so i can find the number of vowels in it\n')
    sum2, vowels_found = vowel_search(sentence)
    print ('the sum of vowels found is ' + str(sum2) + 'and the list of them is  ' + str(vowels_found))
    

if __name__ == '__main__':
    main()
