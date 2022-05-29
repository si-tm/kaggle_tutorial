import pandas as pd

def main():
    # save filepath to variable for easier access
    melbourne_file_path = './melb_data.csv'
    # read the data and store data in DataFrame titled melbourne_data
    melbourne_data = pd.read_csv(melbourne_file_path) 
    # print a summary of the data in Melbourne data
    print(melbourne_data.describe())
    print(type(melbourne_data.describe()))

if __name__ == '__main__':
  main()