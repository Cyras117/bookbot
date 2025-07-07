def get_num_words(text):
    """
    Counts the number of words in a given text string.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The number of words in the input text.
    """
    words = text.split()
    return len(words)

#sort_on = lambda itens: itens['count']  # This is a lambda function to sort by count
# Using a named function instead of a lambda for better readability
def sort_on(itens):
    return itens['count']

def get_letters_from_text(text):
    """
    Counts the frequency of each letter in the given text.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary where keys are lowercase alphabetic characters and values are their respective counts in the text.

    Example:
        >>> get_letters_from_text("Hello, World!")
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

    Notes:
        - The function is case-insensitive; all letters are converted to lowercase.
        - Only alphabetic characters (a-z) are counted; other characters are ignored.
    """
    letters={}
    for char in text.lower():
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
    return letters

def letters_dict_to_list(letters_dict):
    """
    Converts a dictionary of letter counts into a list of dictionaries.

    Args:
        letters_dict (dict): A dictionary where keys are letters (str) and values are their counts (int).

    Returns:
        list: A list of dictionaries, each containing:
            - "name": the letter (str)
            - "count": the number of occurrences (int)

    Example:
        >>> letters_dict = {'a': 2, 'b': 3}
        >>> letters_dict_to_list(letters_dict)
        [{'name': 'a', 'count': 2}, {'name': 'b', 'count': 3}]
    """
    letters_list = []
    for key, value in letters_dict.items():
        letters_list.append({"name": key, "count": value})
    return letters_list

def get_letter_count(text):
    """
    Returns a sorted list of letter counts from the given text.

    Args:
        text (str): The input string to analyze.

    Returns:
        list: A list of dictionaries, each containing:
            - "name": the letter (str)
            - "count": the number of occurrences (int)
        The list is sorted in descending order by count.

    Example:
        >>> get_letter_count("Hello, World!")
        [{'name': 'l', 'count': 3}, {'name': 'o', 'count': 2}, ...]
    """
    letters = get_letters_from_text(text)
    letters_dict = letters_dict_to_list(letters)
    letters = sorted(letters_dict, key=sort_on, reverse=True)
    return letters
