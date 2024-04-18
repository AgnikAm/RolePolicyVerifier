from json import load, JSONDecodeError

def load_json_from_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return load(file)
        
    except JSONDecodeError as e:
        print(f'Decoding error: {e}')
        exit(1)

    except FileNotFoundError as e:
        print(f'File {file_path} not found')
        exit(1)