def separate_movies_tvshows(dataset,selection):
    """Function that divides the given dataset into movies and tv shows
    
    Args:
        dataset

    Returns:
        disney_movies & disney_shows   
    """
    disney_movies = []
    disney_shows = []
    others = []

    for row in dataset:
        type = row[1].lower()
        if type.startswith("movie") and selection == 'm':
            row[1] = "Movie"
            disney_movies.append(row)
        elif type.startswith("tv") and selection == 't':
            row[1] = "TV Show"
            disney_shows.append(row)
        else:
            others.append(row)
    
    if selection == 'm':
        return disney_movies
    elif selection == 't':
        return disney_shows
    else:
        return dataset