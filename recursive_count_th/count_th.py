'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

wordup = "thissymbolsthissymbol"

def count_th(word):
    index1 = 0
    index2 = 1
    count = 0
    if(len(word) == 0):
        return 0
    def wordcount(word, count = 0):
        if(len(word) == 0):
            print(count)
            return count
        elif(word[index1:index2 + 1] == "th"):
            print(word[index1:index2 + 1])
            count += 1
            nextword = word[index2:]
            print(nextword)
            return wordcount(nextword, count)
        else:
            nextword = word[index2:]
            print(nextword)
            return wordcount(nextword, count)
    return wordcount(word, count)
    

count_th(wordup)