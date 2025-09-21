def count_book_words(book_contents: str):
    list_of_words: list[str] = book_contents.split()
    print(f"Found {len(list_of_words)} total words")


def count_book_characters(book_contents: str):
    charmap: dict[str, int] = {}
    for char in book_contents:
        lower_char = char.lower()
        if lower_char in charmap:
            charmap[lower_char] += 1
        else:
            charmap[lower_char] = 1
    return charmap


def sort_on(dictionary_input: dict[str, str | int]):
    return dictionary_input["num"]


def sort_characters_dictionary(char_dict: dict[str, int]) -> list[dict[str, str | int]]:
    list_of_char_dictionaries: list[dict[str, str | int]] = []
    for key in char_dict:
        if key.isalpha():
            char_and_freq_dict = {"char": key, "num": char_dict[key]}
            list_of_char_dictionaries.append(char_and_freq_dict)
    list_of_char_dictionaries.sort(reverse=True, key=sort_on)

    return list_of_char_dictionaries
