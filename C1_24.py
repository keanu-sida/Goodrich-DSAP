## Write a short function that counts the number of vowels in a given character string.

### initalize a string with all the vowels and a test string
vowels = "aeiouAEIOU"
test = "Let's see how GREAT this function is!" # ans should be 11

### create function that checks each char in chars to see if it is in the vowels string. If so, increment the count.
def vowel_checker(chars):
    count = 0
    for ch in chars:
        if ch in vowels:
            count += 1
    return count

### call function on test string
print(vowel_checker(test))