def tukey_rule(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """ Apply Tukey rule on dataframe to remove rows from dataframe, if outlier is detected in col column_name """
    # Filter the data for the relevant columns
    # Calculate the first quartile of the values in col column_name
    Q1 = df[column_name].quantile(0.25)

    # Calculate the third quartile of the values in col column_name
    Q3 = df[column_name].quantile(0.75)

    # Calculate the interquartile range Q3 - Q1
    IQR = Q3 - Q1

    # Calculate the maximum value and minimum values according to the Tukey rule
    max_value = Q3 + 1.5 * IQR
    min_value = Q1 - 1.5 * IQR
    
    # filter df for values that are less than max_value and greater than min_value
    df = df[(df[column_name] > min_value) & (df[column_name] < max_value)]
    
    return df
