def explore_data(data_list_l, start_l, end_l, rows_and_columns_l):
    """Function that explores the data and returns the data between given start and end rows. Also, it displays total number of rows and columns if set as True. By default, it is set to False.
    
    Args:
        data_list, starting row, ending row(exclusive) and flag to check if number of rows and columns are to be displayed.

    Returns:
        sliced data_list and of flag is set then number of columns and rows.
        
    """
    if end_l == None:
        data_slice_l = data_list_l[start_l:]
    else:
        data_slice_l = data_list_l[start_l:end_l]
        
    for row_l in data_slice_l:
        print(row_l)
        print('\n')
        
    if rows_and_columns_l:
        print('no. of rows:', len(data_list_l))
        print('no. of columns:', len(data_list_l[0]))