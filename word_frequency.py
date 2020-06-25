import re
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # Your code will go here. You can write additional functions if you want, and call them inside this function.
    # first open the file
    with open(file,"r") as f:
        text_string = f.read().lower()
    frequency = {}
    match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string)
    for word in match_pattern:
      count = frequency.get(word, 0)
      frequency[word] = count + 1
    frequency_list = frequency.keys()
    print(frequency)
    for words in frequency_list:
        print(words,frequency[words])

        # lyrics = f.readlines()
        # word_list = [line.split() for line in lyrics]
        # print(word_list)

# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
