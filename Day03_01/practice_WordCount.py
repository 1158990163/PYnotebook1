import sys
import re


def Statistics_word(filename):
    with open(filename, 'r', encoding='utf-8')as f:
        line = f.read().lower()
        for i in r',.?,)\'\"(`!:-*_;\\':
            line = line.replace(i, '')
        words_noSet = list(line.split())
        words_Set = list(set(line.split()))
        wordlist = []
        temp = 0;
        for i in words_Set:
            for j in words_noSet:
                if i == j:
                    temp += 1
            wordlist.append((i, temp))
            temp = 0
    return wordlist


def print_words(filename):

    word_list = Statistics_word(filename)
    for i in range(len(word_list)):
        print(word_list[i][0], word_list[i][1])



def print_top(filename):
    temp = 0
    word_list = Statistics_word(filename)
    for i in range(len(word_list)):
        word_list[i] = word_list[i][::-1]
    word_list.sort(reverse=True)
    for i in range(len(word_list)):
        if temp==20:
            break
        print(word_list[i][1], word_list[i][0])
        temp+=1



def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
