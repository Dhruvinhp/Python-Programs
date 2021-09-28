# import re
# import collections


# def freq(str):
#     str_list = str.split()
#     unique_words = set(str_list)
#     for words in unique_words:
#         print(str_list.count(words), ':', words)


# if __name__ == "__main__":
#     str = 'This is a great example of how this task can be done. It should be done in a way that shows it is done with the details and how it works. '
#     freq(str)

# # d, w = "This is a great example of how this task can be done. It should be done in a way that shows it is done with the details and how it works.", [
# #     "this", "is", "are", "it"]

# # pattern = re.compile("|".join(w), flags=re.IGNORECASE)
# # print(collections.Counter(pattern.findall(d)))
def freq(str):

    # break the string into list of words
    str = str.split()
    str2 = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in str2:

            # insert value in str2
            str2.append(i)

    for i in range(0, len(str2)):

        # count the frequency of each word(present
        # in str2) in str and print
        print(str.count(str2[i]), ': ', str2[i], 'is :',)


def main():
    str = 'This is a great example of how this task can be done. It should be done in a way that shows it is done with the details and how it works. '
    freq(str)


if __name__ == "__main__":
    main()
