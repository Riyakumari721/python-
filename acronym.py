def create_acronym(input_string):
    words = input_string.split()
    acronym = ""

    for word in words:
        acronym += word[0].upper()

    return acronym

input_string = input("Enter a string: ")
acronym = create_acronym(input_string)

print("Acronym:", acronym)



