def average(data_l,loc_l):
    """Calculates the average of the values in given column

    Args:
        data, column location

    Returns:
        average of all the values
        
    """
    sum_l = 0
    count_l = 0
    for row_l in data_l:
        sum_l += row_l[loc_l]
        count_l += 1
    return(sum_l/count_l)