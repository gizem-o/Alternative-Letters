
sentence = input("Please enter a sentence: ")
final_sentence = ""

for i in range(len(sentence)):
    if i % 2 == 1:  # Odd characters (so starting from second character)
        final_sentence += sentence[i].lower()  # Will become lower case
    else:
        # Even characters (so every other character), will become upper case
        final_sentence += sentence[i].upper()
print(final_sentence)

sentence_list = (sentence.split())
new_sentence = ""

for i in range(len(sentence_list)):
    if i == " ":
        continue
    elif i % 2 == 1:
        # Odd strings (starting from second string (1) will become lower case)
        new_sentence += sentence_list[i].lower()
        # Space is added after every string
        new_sentence += " "
    else:
        # Even strings (starting from first string (0) will become upper case)
        new_sentence += sentence_list[i].upper()
        # Space is added after every string
        new_sentence += " "

print(new_sentence)

