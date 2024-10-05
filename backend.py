FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """
    Read a text file and return the list of to-do items.

    :param filepath: Path to the to-do file
    :return: List of to-do items
    """
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return []


def write_todos(todos, filepath=FILEPATH) -> None:
    """
    Write the to-do items list to the text file.

    :param todos: List of to-do items
    :param filepath: Path to the to-do file
    """
    with open(filepath, "w") as file:
        file.write("\n".join(todos))