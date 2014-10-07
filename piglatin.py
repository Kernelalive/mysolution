def is_vowel(char):
    the_vowels = ['a', 'e', 'i', 'o', 'u']
    for i in the_vowels:
        if char in the_vowels:
            return True
        else:
            return False


def piglatin(wor):
    if (is_vowel(wor[0].lower())) :
        wor = wor[1:len(wor)] + wor[0] + 'way'
    else:
        wor = wor[1:len(wor)] + wor[0] + 'ay'
    print (wor)

    main()
    


def main():
    word = raw_input('Enter a word to start the pig latin game\n')
    piglatin(word)

if __name__ == '__main__':
    main()
    
                     
