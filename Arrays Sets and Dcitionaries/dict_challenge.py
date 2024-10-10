#Write a program that prints the character that occurs the mostin the string
#also print the number of times the character occurs in the string
#sentence = "This is a common interveiw question"
#print(sentence)
#
#def start() -> None:
#    print(len(sentence))
#    for c in sentence:
#        if c.isalpha():
#            print(set(c))
#            print(sentence.count(c))
#    return
#pass
#start()


sentence = "This is a common interview question"
print(sentence)

def find_most_common_char(s: str) -> None:
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    for c in s:
        if c.isalpha():  # Count only alphabetic characters
            c = c.lower()  # Consider case insensitivity
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    
    # Find the character with the maximum count
    most_common_char = max(char_count, key=char_count.get)
    most_common_count = char_count[most_common_char]
    
    print(f"The most common character is '{most_common_char}' which occurs {most_common_count} times.")

find_most_common_char(sentence)












