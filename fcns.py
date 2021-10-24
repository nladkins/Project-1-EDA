# this file will be where i write all of my functions so that they dont clutter up the actual scripts


def column_connector(col_name, df, return_df):
    """
    Args:
        col_name (str): name of column in the raw data that you want to get the full name of.
        df: the raw data dataframe
        return_df: the dataframe containing the labels you want to return.

    Returns: the column name from the labels dataframe.

    Examples:
        column_connector('age') returns 'Age bracket (in years)'

        a = 'age'
        column_connector('a') returns 'Age bracket (in years)'

        column_connector(age) will raise an exception.
    """
    try:
        col_idx = df.columns.get_loc(col_name)
        returned_name = return_df.columns[col_idx]
        return returned_name
    except NameError:
        print('the column name passed to the fcn must be a str or a variable holding a str.')


def filter_data(df, filter_val, filter_column):
    """
    Args:
        df: the dataframe you want to search.
        filter_val: the value you want to find and keep visible after filtering.
        filter_column: the column you want to check for the value in

    Returns:
        the filtered dataframe only showing the values you want to see.

    Examples:
        filter_data(df_raw, 7, 'age') returns a dataframe only showing people >75 (because 7 is the int that
        corresponds to >75)
    """

    filtered_df = df[df[filter_column] == filter_val]
    return filtered_df


def value_connector(lookup_val, lookup_col, return_col):
    """
    Args:
        lookup_val: the value from the raw data you want to lookup
        lookup_col: the name of the column holding your lookup value
        return_col: the name of the column you want to pull the corresponding value from.
    Returns:
        the equivalent value from the labels column

    Note: to avoid having to manually find the filter_column, use this fcn with column_connector.

    Examples:
        import fcns as f
        f.value_connector(1, df_raw['age'], df_labels[(f.column_connector('age'))])

        will return
        The above uses the column_connector to retrieve the name of the df_labels column you're interested in.
        This is much simpler than manually looking up and comparing column names.
    """
    output_dict = dict(zip(lookup_col.unique(), return_col.unique()))
    output = output_dict[lookup_val]
    return output