# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

from collections import deque
import time


# Breadth First Search (BFS)
def shortest_word_chain(word1, word2):
    if len(word1) < 3 or len(word2) < 3:
        raise ValueError("Words must have at least 3 letters")

    with open("wordsEn.txt", "r") as file:
        word_list = file.read().splitlines()

    word_list = [w for w in word_list if len(w) >= 3]

    word_keys = {}
    for word in word_list:
        if word[:2] not in word_keys:
            word_keys[word[:2]] = []
        word_keys[word[:2]].append(word)

    # Initialize queue with the first word
    queue = deque([(word1, [word1])])
    visited = set([word1])

    while queue:
        current_word, path = queue.popleft()

        # If the last 2 characters of the current word match the first 2 characters of the target word
        if current_word[-2:] == word2[:2]:
            return path + [word2]

        # Add all adjacent words to the queue
        start_key = current_word[-2:]
        if start_key in word_keys:
            for word in word_keys[start_key]:
                if word not in visited:
                    visited.add(word)
                    queue.append((word, path + [word]))
                    # queue.appendleft((word, path + [word])) # DFS

    return None  # Không tìm thấy chuỗi


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
time_start = time.time()
print("\n".join(shortest_word_chain(word1, word2)))
time_end = time.time()
print(f"Time taken: {time_end - time_start} seconds")
