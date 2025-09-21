import sys
from stats import count_book_words, count_book_characters, sort_characters_dictionary


def get_book_text(file_path: str) -> str:
    book_contents: str = ""
    with open(file_path) as book_path:
        book_contents = book_path.read()

    return book_contents


def main():
    system_arguments = sys.argv
    if len(system_arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_contents = get_book_text(sys.argv[1])
    char_dictionary: dict[str, int] = count_book_characters(book_contents)
    sorted_dictionaries_by_freq: list[dict[str, str | int]] = (
        sort_characters_dictionary(char_dictionary)
    )
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_book_words(book_contents)
    print("--------- Character Count -------")
    for i in range(len(sorted_dictionaries_by_freq)):
        print(
            f"{sorted_dictionaries_by_freq[i]['char']}: {sorted_dictionaries_by_freq[i]['num']}"
        )


main()
