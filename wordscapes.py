# print all dictionary words that can be formed using a set of letters

words_file = open('wordsEn.txt')
text = words_file.read()
words = text.split("\n") # list of words in dictionary
dictionary = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],
       'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [],
       'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [],
       's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [],
       'y': [], 'z': [],
       }

def create_dictionary():
    pos = 0
    for key in dictionary.keys():
        for i in range(pos, len(words)):
        	if key == words[i][0]:
        		dictionary[key].append(words[i])
        	else:
        		pos = i
        		break

create_dictionary()

def show_wordscapes(letters, min_len=3):
    
    letters = [x for x in letters]
    def valid(word):
        test = letters + []
        for l in word:
            if l not in test:
                return False
            else:
                test.remove(l)
        return True

    for l in set(letters):
        for word in dictionary[l]:
            for i in range(min_len, len(letters) + 1):
                if len(word) == i and valid(word):
                    print(word)
