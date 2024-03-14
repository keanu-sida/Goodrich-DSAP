## Write a short Puthon function that takesa string s, representing a sentence, and returns a copy of the string with all punctuation removed (e.x. "Let's try, Mike" -> "Lets try Mike")

### declare a string with all punctuation characters, and a test string to be modified
punctuation = ".?,;:-[]\{\}()\"\'!"
test  = 'Let\'s try, \'big\' Mike.'

### define a function which tests each character in a string to see if it's in the punctuation string. If so, replace it with an empty string. Then, return it.
def punctuation_remover(chars):
    for i in chars:
        if i in punctuation:
            chars = chars.replace(i, "", 1)
    return chars

### print the result to test for accuracy
print(punctuation_remover(test))