import pandas as pd
from sklearn.tree import DecisionTreeRegressor

def select_data_for_modeling(df):
    # a list of all columns in the dataset.
    print(df.columns)
    # Nanを削除
    # df = df.dropna(axis=0)
    print(df.describe())
    y = df.Price
    print(y)
    return y

def choosing_features(df):
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = df[melbourne_features]
    print(X.describe())
    print(X.head())
    print("Making predictions for the following 5 houses:")
    return X

def building_my_model(df):
    # Define model. Specify a number for random_state to ensure same results each run
    melbourne_model = DecisionTreeRegressor(random_state=1)
    X = choosing_features(df)
    y = select_data_for_modeling(df)
    # Fit model
    print(X)
    print(y)
    print(type(melbourne_model))
    melbourne_model.fit(X, y)
    print(X.head())
    print("The predictions are")
    print(melbourne_model.predict(X.head()))
    print("Making predictions for the following 5 houses:")
    print(X.head())
    print("The predictions are")
    print(melbourne_model.predict(X.head()))


def main():
    melbourne_file_path = './melb_data.csv'
    melbourne_data = pd.read_csv(melbourne_file_path) 
    # select_data_for_modeling(melbourne_data)
    # choosing_features(melbourne_data)
    building_my_model(melbourne_data)

    


if __name__ == '__main__':
  main()

