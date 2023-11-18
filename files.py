import os

print('dir', os.getcwd())
dir = 'folder'

# # if not os.path.isdir(dir):
# #     os.mkdir(dir)
# # else:
# #     print('Такая папка уже существует')
# #
# # os.chdir('folder')
# # print('dir', os.getcwd())
# #
file = open('folder/article.txt', 'a')
# # file.write('\nqwertynoqwerty')
#
# # os.rename('text.txt', 'new_text.txt')
# # os.replace('./folder/new.txt', '../new_text.txt')
# # os.remove('folder')
# # for path, dirs, files in os.walk('../venv'):
# #     for dir in dirs:
# #         print(os.path.join(path, dir))
# #     for file in files:
# #         print(os.path.join(path, file))
#
# # os.rmdir('folder')
# # print(os.stat('files.py').st_size)
# with open('.folder'):
#     pass

# ======================================================================================================================

# 1
print('#1')


def read_end(lines, file):
    with open(file, encoding='utf-8') as f:
        listF = f.readlines()
    st = ''
    if lines < 0:
        return 'Количество строк должно быть положительным'
    for i in range(len(listF) - lines, len(listF)):
        st += listF[i]
    return st


f = read_end(3, 'folder/article.txt')
print(f + 'rqwrqw' + 'eqwrqwrwqrqw', end='')

# ----------------------------------------------------------------------------------------------------------------------

# 2
print('\n\n#2')


def print_reps(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(item_path + '/')
            print_reps(item_path)
        else:
            print(item)


print_reps('./venv/Scripts')

# ----------------------------------------------------------------------------------------------------------------------

# 3
print('\n#3')


def longest_word(file):
    with open(file, encoding='utf-8') as f:
        listF = f.readlines()
    maxL = 0
    listMax = []
    sepList = ',.;:-—!?'
    clearLs = []
    for sent in listF:
        st = ''
        for w in sent:
            if w not in sepList:
                st += w
        clearLs.append(st)
    for sent in clearLs:
        listSt = sent.split()
        for item in listSt:
            if maxL < len(item):
                maxL = len(item)
                listMax = []
            if len(item) == maxL:
                listMax.append(item)
    print(listMax)


longest_word('folder/article.txt')

# ----------------------------------------------------------------------------------------------------------------------

# 4
print('\n#4')


def text_statistics(file):
    with open(file, 'r') as f:
        text = f.read()

    letter_count = sum(1 for char in text if char.isalpha())
    word_count = len(text.split())
    line_count = text.count('\n') + 1

    print("Input file contains:")
    print(f"{letter_count} letters")
    print(f"{word_count} words")
    print(f"{line_count} lines")


text_statistics('folder/file.txt')
