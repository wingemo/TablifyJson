# main.py
from .utils.utils import json_to_table, print_table

def main(json_input='{}'):
    df = json_to_table(json_input)
    print_table(df)

if __name__ == "__main__":
    # Example JSON input
    json_input = '{"name": "John", "age": 30, "city": "New York"}'
    main(json_input)