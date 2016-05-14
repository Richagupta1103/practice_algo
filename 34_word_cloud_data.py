'''
You want to build a word cloud, an infographic where the size of a word
corresponds to how often it appears in the body of text.
To do this, you will need data. Write code that takes a long string and builds
 its word cloud data in a dictionary , where the keys are words and the values
 are the number of times the words occured.

Think about capitalized words. For example, look at these sentences:

After beating the eggs, Dana read the next step:
Add milk and eggs, then add flour and sugar.
What do we want to do with "After", "Dana", and "add"?
In this example, your final dictionary should include one
"Add" or "add" with a value of 22. Make reasonable (not necessarily perfect
) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
'''


class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()

        current_word = ''
        for i in range(0, len(input_string)):

            character = input_string[i]

            # if we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string)-1:
                if self.is_letter(character): current_word += character
                if current_word: self.add_word_to_dictionary(current_word)

            # if we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word: self.add_word_to_dictionary(current_word)
                current_word = ''

            # we want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string)-1 and input_string[i+1] == '.':
                    if current_word: self.add_word_to_dictionary(current_word)
                    current_word = ''

            # if the character is a letter or an apostrophe, we add it to our current word
            elif self.is_letter(character) or character == '\'':
                current_word += character

            # if the character is a hyphen, we want to check if it's surrounded by letters
            # if it is, we add it to our current word
            elif character == '-':
                if i > 0 and self.is_letter(input_string[i-1]) and \
                        self.is_letter(input_string[i+1]):
                    current_word += character
        return self.words_to_counts

    def add_word_to_dictionary(self, word):

        # if the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # if an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1

    def is_letter(self, character):
        return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

string = "After beating The eggs Dana read The next step's"
obj = WordCloudData(string)
print obj.words_to_counts





# class WordCloudData:
#     def __init__(self,string):
#         self.word_to_count = {}
#         self.populate_word_from_string(string)
#
#     def populate_word_from_string(self,string):
#         current_word = ''
#         for i in range(len(string)):
#             character = string[i]
#             if i == len(string)-1:
#                 if self.is_letter(character):
#                     current_word += character
#                 if current_word:
#                     self.add_to_dictionary(current_word)
#
#             elif character == " " or character == u'\u2014' :
#                 if current_word:
#                     self.add_to_dictionary(current_word)
#                     current_word = ''
#
#             elif self.is_letter(character) or character == '\'':
#                 current_word += character
#
#             elif character == '-':
#                 if i > 0 and self.is_letter(string[i-1]) and self.is_letter(string[i+1]):
#                     current_word += character
#
#
#
#     def add_to_dictionary(self,word):
#
#         if word in self.word_to_count:
#             self.word_to_count[word] += 1
#         elif word.lower() in self.word_to_count:
#             self.word_to_count[word] += 1
#         elif word.capitalize() in self.word_to_count:
#             self.word_to_count[word] = 1
#             self.word_to_count[word] += self.word_to_count[word.capitalize()]
#             del self.word_to_count[word.capitalize()]
#         else:
#             self.word_to_count[word] = 1
#
#
#     def is_letter(self, character):
#         return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#
# string = "After beating Th1e eggs Dana read the next step's"
# obj = WordCloudData(string)
# print obj.word_to_count