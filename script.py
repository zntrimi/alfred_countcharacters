import sys
# word would be query :
word = sys.argv[1]


word = word.replace(' ', '')

word = word.replace('　', '')

word = word.replace('\n', '')

query = len(word.strip())


sys.stdout.write(str(query))
