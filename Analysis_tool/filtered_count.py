from filter_data import filter_data

def items_count(dataset_l, loc_l, sep_l, filters_l):
    """Give the list of unique values with it's count sorted in descending order. The column might contain the list of values separated by separator. Also, you can specify any number of filtering criteria in the form of dictionary where key would be the column location and value would be filtering value.

    Args:
        dataset, column location, separator for values in given column, filter criteria dictionary
    Returns:
        Unique Values along with it's count in descending order
        
    """
    items_count_l = {}
    for row_l in dataset_l:
        if filters_l != {}:
            include_row_l = filter_data(row_l, filters_l)
        else:
            include_row_l = True
        if include_row_l:
            items_list_l = row_l[loc_l].split(sep_l)
            for item_l in items_list_l:
                if item_l.strip() in items_count_l:
                    items_count_l[item_l.strip()] += 1
                else:
                    items_count_l[item_l.strip()] = 1
    sorted_items_count = dict(sorted(items_count_l.items(), key=lambda item: item[1], reverse=True))
    return sorted_items_count