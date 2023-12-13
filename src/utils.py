from prettytable import PrettyTable

"""A bunch of useful code utilities."""


def print_table(data, headers):
    """
    Prints a table with the given data and headers
    
    """
    table = PrettyTable()
    table.field_names = headers
    for row in data:
        table.add_row(row)
    return table