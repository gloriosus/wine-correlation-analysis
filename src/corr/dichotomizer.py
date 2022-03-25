import pandas

def get_dichotomized_data(dataframe, column: str) -> pandas.DataFrame:
    dataset = dataframe

    length = len(dataset.index)

    for i in range(length):
        if dataset.loc[i, column] <= 5:
            dataset.loc[i, column] = 0
        else:
            dataset.loc[i, column] = 1

    return dataset