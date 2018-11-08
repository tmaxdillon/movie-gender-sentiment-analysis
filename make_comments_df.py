from urllib import request
from os import listdir
import pandas as pd

PATH = "comments"
def make_dfs():
    filenames2 = find_csv_filenames(PATH)
    for name in filenames2:
        print(name)
        new_name = PATH+"/"+name
        df = pd.read_csv(new_name, encoding ='latin1')
        my_df = pd.DataFrame(data = df)
        print(my_df.head())
    return my_df


def find_csv_filenames(path_to_dir, suffix=".csv"):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
    


make_dfs()