pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
    
word = original.lower()
word = original.upper()[0]
first = word[0]

new_word= word[1:len(word)]+first+pyg
print new_word


