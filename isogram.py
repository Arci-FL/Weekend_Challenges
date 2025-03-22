#Isogram

print("ISOGRAM CHECKER")
word = input("Please enter the word to be checked: ")
count = 0

# for loop to get the number of matches between the same word.
# the number of matches can never be less than length of the string.
# but it can be greater
'''
for example: the user enters `bead`. If we look for the number of times the letters in `bead` matches
with the same word `bead`, it equals 4.
In the case of a user input, `seed`, the letters in seed match with the same letters in the same word
6 times.
This proves similar for other words with repeating letters (non-isograms), as such, if the number of
matches is larger than the actual word, it has repeating letters, thus we can conclude they are
not Isograms.
'''

for i in word:
    for j in word:
        if (i == j):
            count +=1

if (count <= len(word) ):
    print("True. ", word , " is an isogram.")
else:
    print("False. ", word , " is NOT an isogram.")
