word_dict = {}
with open('Python.py') as file:
    content = file.readlines()
for line in content:
    words = line.split(' ')
for word in words:
    word = word.strip().lower()
    if word not in word_dict:
        word_dict[word] = 0
        word_dict[word] += 1
        top_ten = sorted(word_dict, key=word_dict.get, reverse=True)[:10]
        print('Highest ten frequencies')
print(' ')
for item in top_ten:
    print(f'{item:10} : {word_dict[item]:2}')
