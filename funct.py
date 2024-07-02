def find_last_slash_index(filepath):

    number_of_slashes = filepath.count('/')
    slash_count = 0

    for index, char in enumerate(filepath):
        if char == '/':
            slash_count +=1
            if slash_count == number_of_slashes:
                return filepath[index:] 