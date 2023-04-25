def list_of_items(data_l, loc_l, sep_l):
    """Function to generate list of unique values. In one row there could be list of multiple values in given column separated by separator.
    
    Args:
        data, column location and separator to look for in the value list in that column

    Returns:
        unique values 
        
    """
    items_list_l = []
    for row_l in data_l:
        if sep_l != '':
            row_list_l = []
            row_list_l = row_l[loc_l].split(sep_l)
            for item in row_list_l:
                if item not in items_list_l:
                    items_list_l.append(item)
        else:
            if row_l[loc_l] not in items_list_l:
                items_list_l.append(row_l[loc_l])
    return items_list_l