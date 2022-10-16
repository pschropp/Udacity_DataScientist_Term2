class Normalizer:    # The normalizer class receives a dataframe as its only input for initialization
    """ Normalize data.
    
    Usage:
    gdp_normalizer = Normalizer(df_2016[['gdp', 'population']])
    x_min, x_max = gdp_normalizer.params
    gdp_normalizer.normalize_data([13424475000000.0, 1300000000])
    """


def __init__(self, dataframe):
    self.params = []

    # iterate through each column calculating the min and max for each column
    for col in dataframe.columns:
        # Append the list to the params variable
        self.params.append(x_min_max(dataframe[col]))


def x_min_max(data):
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum


def normalize_data(self, x):
    # The function receives a data point as an input and then outputs the normalized version
    normalized = []

    for i, value in enumerate(x):
        x_max = self.params[i][1]
        x_min = self.params[i][0]
        normalized.append((x[i] - x_min) / (x_max - x_min))
    return normalized
