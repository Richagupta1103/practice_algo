'''
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into
a major European National Cake Vault. The message has been mostly deciphered, but all
the words are backwards! Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a string message and reverses the order of the words in-place
'''


def reverse_word(string):
    string = string.split()
    for word in string[::-1]:
        print word,

message = 'find you will pain only go you recordings security the into if'
reverse_word(message)
