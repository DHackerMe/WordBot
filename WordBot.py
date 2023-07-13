import os

def find_words(letters):
    words_found = []
    letter_count = {letter: letters.count(letter) for letter in set(letters)}
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'words.txt')
    
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip().lower()
            word_count = {letter: word.count(letter) for letter in set(word)}
            
            if all(word_count.get(letter, 0) <= letter_count.get(letter, 0) for letter in set(word)) and len(word) <= len(letters):
                words_found.append(word)
    
    return words_found

user_letters = input("Input the letters: ").lower()

words_found = find_words(user_letters)

if words_found:
    print("Words found:")
    for word in words_found:
        print(word)
else:
    print("No words found.")
