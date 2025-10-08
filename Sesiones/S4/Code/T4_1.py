from typing import Generator

def data_generator_from_file(file_path: str) -> Generator:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            _line = line.strip()
            if _line:
                yield _line

def print_navaid_data(qty: int) -> None:
    file_path = 'Data/api_response.txt'
    data_gen = data_generator_from_file(file_path)
    count = 0

    try:
        while count < qty:
            current = next(data_gen)
            if current.startswith('//'):
                continue
            print(current)
            count += 1
    except StopIteration:
        return

if __name__ == '__main__':
    print_navaid_data(10)
