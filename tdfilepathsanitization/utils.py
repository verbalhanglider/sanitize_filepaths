
from pathlib import Path
from os import sep

def whitelist_approved_chars(some_path_as_string):
    new_word = []
    for character in some_path_as_string:
        if character in ['/', '\\', ':']: 
            new_word.append(character)
        elif character.isalnum():
            new_word.append(character)
        else:
            raise ValueError("invalid character in your path")
    return ''.join(new_word)

def remove_unsafe_path_traversal_commands(some_path_as_string):
    words_list = some_path_as_string.split(sep)    
    new_words_list = []
    for word in words_list:
        if not '..' in word:
            new_words_list.append(word)
    return '{}'.format(sep).join(new_words_list)

def are_the_parents_extant(some_path_as_string):
    path = Path(some_path_as_string)
    logical_parents = path.parents 
    for np in logical_parents:
        if not np.exists():
            msg = "{} is a parent of your path, but it does not exist".format(np.as_posix())
            raise ValueError(msg)
    return some_path_as_string

def does_the_path_exist_already(some_path_as_string):
    testable = Path(some_path_as_string)
    return testable.exists()

def create_unextant_parents(some_path_as_string):
    logical_parents = Path(some_path_as_string).parents
    for parent in logical_parents:
        create_directory(parent.as_posix())
    return some_path_as_string

def create_directory(some_path_as_string):
    path = Path(some_path_as_string)
    if not path.exists():
        path.mkdir()
    return some_path_as_string