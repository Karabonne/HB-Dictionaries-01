def get_word_list(file_name):

    master_word_list = []

    with open(file_name) as file:
        fh = file.readlines()

    for line in fh:
        line = line.rstrip()
        word_list_line = line.split(":")
        for word in word_list_line:
            master_word_list.append(word)

    return master_word_list

def word_counter(file_name):
    """ Counts occurences of each word and adds to the dictionary."""
    word_counts = {}    

    for word in get_word_list(file_name):
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(f"{word} {count}")

    return word_counts