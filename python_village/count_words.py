
def count_words(words):
    word_map = {}
    for word in words:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    return word_map


def print_map(word_map):
    for word, count in word_map.items():
        print('{} {}'.format(word, count))


words_list = open('count_words.txt').read().split(' ')
count_map = count_words(words_list)
print_map(count_map)
