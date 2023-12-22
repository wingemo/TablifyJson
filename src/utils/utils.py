# utils.py
import pandas as pd
import json
from tabulate import tabulate

def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        else:
            items[new_key] = value
    return items

def json_to_table(json_str):
    try:
        data = json.loads(json_str)
        if isinstance(data, list):
            return pd.DataFrame.from_records(data)
        elif isinstance(data, dict):
            if all(isinstance(value, list) for value in data.values()):
                return pd.DataFrame.from_dict(data)
            else:
                flat_data = flatten_dict(data)
                df = pd.DataFrame([flat_data])
                return df
        else:
            raise ValueError("Invalid JSON input")
    except ValueError as e:
        raise ValueError("Invalid JSON input")

def print_table(df):
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
