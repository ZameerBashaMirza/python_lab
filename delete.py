text = input("Please enter any text: ").lower()
letters = []
letters.append(input("enter any letter: ").lower())
letters.append(input("enter any letter: ").lower())
letters.append(input("enter any letter: ").lower())

print("\n")
print("REPETITION OF LETTERS")

print(f"No of times this letter {letters[0]}:{text.count(letters[0])} times")
print(f"No of times this letter {letters[1]}:{text.count(letters[1])} times")
print(f"No of times this letter {letters[2]}:{text.count(letters[2])} times")

print("\n")
print("WORDS IN TEXT")

no_of_words = text.split()
print(len(no_of_words))

print("\n")
print("FIRST AND LAST LETTER OF THE TEXT")
first = text[0]
last = text[-1]
print(f"first letter: {first}\n last letter: {last}")

print("\n")
print("WORDS IN INVERTED ORDER")

no_of_words.reverse()
inverted_text = " ".join(no_of_words)
print(inverted_text)

print("\n")
print("LOOKING FOR THE WORD PYTHON")

check = 'python' in text
check_in = {
    True: 'was',
    False: 'was not'
}
print(f"The word is 'python' {check_in[check]} available")
