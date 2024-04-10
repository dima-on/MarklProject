"""
Нейронка на основе Маркла.
Автор: Дмитрий Онуфриев
Дата создания: 05.04.2024
"""

import random

import pandas as pd


all_words: list[str] = []
after_words: list[list[str]] = []
after_words_count: list[list[int]] = []


def learn_function():
    """Read and Lern"""
    with open("test.txt", "r", encoding="utf-8") as file:
        lern_input = file.read()
    all_words = lern_input.split()
    return all_words


words = learn_function()


def check_fullstop(simvol) -> bool:
    """Check which words has fullstop"""
    for one_simvol in simvol:
        if one_simvol in (".", "?"):
            return False
    return True


def check_set_words(simvol):
    """Check which words being"""

    i_count = 0
    for sim in all_words:
        if simvol == sim:
            return i_count
        i_count += 1
    return -1


def check_set_next_words(simvol, index_word):
    """Check which next words being"""

    i_count = 0
    for words_in in after_words[index_word]:
        if simvol == words_in:
            return i_count
        i_count += 1

    return -1


def write_new_words(count_for_in_check, next_word):
    """Write new words to array"""
    after_words[count_for_in_check].append(next_word)
    after_words_count[count_for_in_check].append(1)


def check_new_words(count_for_in_check, index_word):
    """Add new next words for array"""
    index_words = check_set_next_words(words[count_for_in_check + 1], index_word)
    if index_words >= 0:
        after_words_count[index_word][index_words] += 1
    else:
        after_words[index_word].append(words[count_for_in_check + 1])
        after_words_count[index_word].append(1)


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

                all_words.append(word)
                after_words.append([])
                after_words_count.append([])
                write_new_words(count_no, words[count_all + 1])

                count_no += 1
        count_all += 1


full_lern()
answer = ""


def make_sentences(new_word):
    """Make sentences and find new word"""
    count_try = 0
    global answer

    for word in all_words:
        if word != new_word:
            count_try += 1
            continue

        good_index = [0]
        new_index = 0

        for count_next_word in after_words_count[count_try]:
            if new_index <= 0:
                continue
            if count_next_word >= after_words_count[count_try][good_index[0]]:
                if count_next_word == after_words_count[count_try][good_index[0]]:
                    good_index.append(new_index)
                else:
                    good_index = [new_index]
            new_index += 1

        next_index = good_index[0]

        if len(good_index) > 1:
            next_index = good_index[random.randrange(0, len(good_index))]

        answer = answer + " " + after_words[count_try][next_index]
        make_sentences(after_words[count_try][next_index])
        break

    return answer


first_word = input("Enter the first")
answer += first_word
answer = make_sentences(first_word)

print()
print(answer)
print()
print(all_words)
print(after_words)
print(after_words_count)


def main():
    pass


if __name__ == "__main__":
    main()
