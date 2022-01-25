from pprint import pprint


# practice Question

sentence = "this is a popular interview question"

storage_dictionary = {}

for everyletter in sentence:
    if everyletter in storage_dictionary:
        storage_dictionary[everyletter] += 1
    else:
        storage_dictionary[everyletter] = 1


sorted_dictionary = sorted(storage_dictionary.items(),
                           key=lambda kv: kv[1],
                           reverse=True)


print(sorted_dictionary)
print(sorted_dictionary[0])
