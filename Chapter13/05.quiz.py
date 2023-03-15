word_list = ["apple", "watch", "apolo", "star", "abocado"]
print(word_list)

words = []
for word in word_list:
    if word[0] == "a":
        words.append(word)

print(words)

first_a = [word for word in word_list if word[0] == "a"]
print(first_a)