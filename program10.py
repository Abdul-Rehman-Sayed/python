def flames(name1, name2):
    name1 = list(name1.lower())
    name2 = list(name2.lower())

    # Remove common letters
    for letter in name1[:]:
        if letter in name2:
            name1.remove(letter)
            name2.remove(letter)

    # Combine remaining letters
    length = len(name1) + len(name2)

    flames = 'FLAMES'
    while len(flames) > 1:
        split_pos = (length - 1) % len(flames)
        flames = flames[split_pos + 1:] + flames[:split_pos]

    if flames == 'F':
        return 'Friends'
    elif flames == 'L':
        return 'Love'
    elif flames == 'A':
        return 'Affection'
    elif flames == 'M':
        return 'Marriage'
    elif flames == 'E':
        return 'Enemy'
    else:
        return 'Sibling'


name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = flames(name1, name2)
print("The relationship is:", result)
