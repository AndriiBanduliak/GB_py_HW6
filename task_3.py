def thesaurus(*args):
    dictionary_names = {}
    list_letters = []

    for name in args:
        list_letters.append(name[0])
    list_letters = list(set(list_letters))
    list_letters.sort()


    for i in list_letters:
        list_names = []
        for name in args:
            if name[0] == i:
                list_names.append(name)
        dictionary_names[i] = list_names
    return dictionary_names


names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(thesaurus(*names))