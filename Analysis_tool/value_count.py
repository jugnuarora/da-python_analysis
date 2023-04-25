def items_count(dataset_l, loc_l, sep_l):
    """Function to generate list of unique values and count of rows with those unique values in given column in descending order of count. In one row there could be list of multiple values in given column seperated by seperator.
    
    Args:
        data, column location and seperator to look for in the value list in that column

    Returns:
        unique values along with count sorted in descending order
        
    """
    items_count_l = {}
    for row_l in dataset_l:
        items_list_l = row_l[loc_l].split(sep_l)
        for item_l in items_list_l:
            if item_l in items_count_l:
                items_count_l[item_l] += 1
            else:
                items_count_l[item_l] = 1
    sorted_items_count = dict(sorted(items_count_l.items(), key=lambda item: item[1], reverse=True))
    return sorted_items_count