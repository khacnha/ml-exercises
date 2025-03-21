# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312

import re
from collections import Counter
def main():
    # Read the file
    with open('story.txt', 'r') as file:
        text = file.read()

    # Remove punctuation characters
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the top 100 words
    top_100_words = word_counts.most_common(100)

    # Print the results
    for word, count in top_100_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
