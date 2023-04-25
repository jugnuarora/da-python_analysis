from average import average
from explore_data import explore_data
from filtered_count import items_count
from unique_values import list_of_items
from separate_movies_tvshows import separate_movies_tvshows
from get_column import get_column_loc
from csv import reader

if __name__ == "__main__":
    
    opened_file = open('../Data/disney_plus_titles.csv', encoding="utf-8")
    read_file = reader(opened_file)
    dp = list(read_file)
    dp_header = dp[0]
    dp = dp[1:]

    # Print a welcome message
    print('Welcome to the world of Data Analysis!')

    # Initialize the flags
    end_of_analysis = False

    # Analysis Loop
    while end_of_analysis == False:

        x = input("To analyze combined dataset type c \nTo analyze only movies type m \nTo analyze only TV shows type t  \nTo quit q \nEnter the option!: ")
        explore_dataset = []
        if x == 'q':
            end_of_analysis = True
            break
        else:
            explore_dataset = separate_movies_tvshows(dp,x)

        y = input("To explore the dataset type e \nTo list the unique values in a column type u \nTo count number of movies/TV shows for each unique values type c \nTo find the average value in a column type a \nEnter the option!: ")

        if y == 'e':
            start = int(input("Give the starting location: "))
            end = input("Give the last row. If you want to display till end of the dataset, just enter: ")
            if end != '':
                end = int(end)
            else:
                end = None
            rows_columns = bool(input("If you want to print number of rows and columns type 1 else press enter"))
            explore_data(explore_dataset, start, end, rows_columns)
        elif y == 'u':
            get_column_loc(dp_header)
            column_loc = int(input('Enter the number as per the list above: '))
            sep = input('Enter the separator in case of multiple values: ')
            print(list_of_items(explore_dataset, column_loc, sep))
        elif y == 'c':
            get_column_loc(dp_header)
            column_loc = int(input('Enter the number as per the list above: '))
            sep = input('Enter the separator in case of multiple values: ')
            filter_flag = input('Are there filter criteria yes/no: ')
            filter_dic = {}
            while filter_flag == 'yes':
                get_column_loc(dp_header)
                input_key = int(input('Enter column to filter as per above list: '))
                print(list_of_items(explore_dataset, input_key, ', '))
                filter_dic[input_key] = input('What value you want to filter: ')
                filter_flag = input('Are there more filter criteria yes/no: ')
            print(items_count(explore_dataset, column_loc, sep, filter_dic))
        elif y == 'a':
            get_column_loc(dp_header)
            column_loc = int(input('Enter the number as per the list above: '))
            print(average(explore_dataset,column_loc))       
        else:
            print('Not a valid option')
        
        print('\n')
