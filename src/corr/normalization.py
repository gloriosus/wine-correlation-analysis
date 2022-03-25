import pandas
from sklearn.preprocessing import PowerTransformer

def get_normalized_data(dataframe, columns_to_transform: list) -> pandas.DataFrame:
    dataset = dataframe

    pt = PowerTransformer()

    dataset.loc[:, columns_to_transform] = pt.fit_transform(dataset.loc[:, columns_to_transform])
    dataset = pandas.DataFrame(data=dataset, columns=dataset.columns)

    return dataset