"""
Нейронка на основе Маркла.
Автор: Дмитрий Онуфриев
Дата создания: 05.04.2024
"""

import random


All_Words = []
After_Words = []
After_Words_Count = []


def lern_function():
    """Read and Lern"""
    with open("test.txt", "r", encoding="utf-8") as file:
        lern_input = file.read()
    all_words = lern_input.split()
    return all_words


words = lern_function()


def check_fullstop(simvol):
    """Check which words has fullstop"""
    for one_simvol in simvol:
        if one_simvol in (".", "?"):
            return False
    return True


def check_set_words(simvol):
    """Check which words being"""

    i_count = 0
    for sim in All_Words:
        if simvol == sim:
            return i_count
        i_count += 1
    return -1


def check_set_next_words(simvol, index_word):
    """Check which next words being"""

    i_count = 0
    for words_in in After_Words[index_word]:
        if simvol == words_in:
            return i_count
        i_count += 1

    return -1


def write_new_words(count_for_in_check, next_word):
    """Write new words to array"""
    After_Words[count_for_in_check].append(next_word)
    After_Words_Count[count_for_in_check].append(1)


def check_new_words(count_for_in_check, index_word):
    """Add new next words for array"""
    index_words = check_set_next_words(words[count_for_in_check + 1], index_word)
    if index_words >= 0:
        After_Words_Count[index_word][index_words] += 1
    else:
        After_Words[index_word].append(words[count_for_in_check + 1])
        After_Words_Count[index_word].append(1)


def full_lern():
    """This function lerns user input"""
    count_all = 0
    count_no = 0
    for word in words:
        if check_fullstop(word):
            index_word_set = check_set_words(word)
            if index_word_set >= 0:
                check_new_words(count_all, index_word_set)

            else:

                All_Words.append(word)
                After_Words.append([])
                After_Words_Count.append([])
                write_new_words(count_no, words[count_all + 1])

                count_no += 1
        count_all += 1


full_lern()
ANSWER = ""


def make_sentences(new_word):
    """Make sentences and find new word"""
    global ANSWER
    count_try = 0
    for word in All_Words:
        if word == new_word:

            good_index = [0]
            new_index = 0

            for count_next_word in After_Words_Count[count_try]:
                if new_index > 0:
                    if count_next_word >= After_Words_Count[count_try][good_index[0]]:

                        if (
                            count_next_word
                            == After_Words_Count[count_try][good_index[0]]
                        ):

                            good_index.append(new_index)
                        else:

                            good_index = [new_index]
                new_index += 1

            next_index = good_index[0]

            if len(good_index) > 1:
                next_index = good_index[random.randrange(0, len(good_index))]

            ANSWER = ANSWER + " " + After_Words[count_try][next_index]
            make_sentences(After_Words[count_try][next_index])

            break
        count_try += 1


FIRST_WORD = input("Enter the first")
ANSWER += FIRST_WORD
make_sentences(FIRST_WORD)

print()
print(ANSWER)
print()
print(All_Words)
print(After_Words)
print(After_Words_Count)
