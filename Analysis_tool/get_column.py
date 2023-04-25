def get_column_loc(column_list):
    """Displays the list of columns and it's corresponding location

    Args:
        data header

    Returns:
        Displays the list of columns
        
    """
    print("Which column:")
    formatted_columns = list(map(lambda x: f"{x[0]}: {x[1]}", zip(range(len(column_list)), column_list)))
    for col in formatted_columns:
        print(col)