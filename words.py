#upper(self, /)


def print_upper_words(words):
    '''Prints capitalized words'''

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    '''Prints capitalized words that start with e and E'''
    
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper)

def print_upper_words3(words, req_letter):
    '''Prints capitalized words that start with the letter you choose'''

    for word in words:
        for letter in req_letter:
            if word.startswith(letter):
                print(word.upper())
                break