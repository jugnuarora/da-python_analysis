def filter_data(row_ll, filters_ll):
    """Selects the row based on list of filter criteria

    Args:
        single row, list of filter criteria in dictionary format where key is the column location and value is the desired value for that column

    Returns:
        True or False based on if it qualifies for the given filter criteria
        
    """
    include_row_ll = True
    for loc_filter_ll, val_filter_ll in filters_ll.items():
        if ',' in row_ll[loc_filter_ll]:
            parts_ll = [part.strip() for part in row_ll[loc_filter_ll].split(',')]
            if val_filter_ll not in parts_ll:
                include_row_ll = False
                break
        else:
            if row_ll[loc_filter_ll] != val_filter_ll:
                include_row_ll = False
                break
    return include_row_ll