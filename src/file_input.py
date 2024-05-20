from json import load


def load_json_from_file(file_path: str) -> dict:
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file to load.

    Returns:
        dict: A dictionary representing the JSON data loaded from the file.
    """
    with open(file_path, 'r') as file:
        return load(file)