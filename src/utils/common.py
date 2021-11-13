import yaml
import os 
import logging
import pandas as pd


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        #print(f"the directory is created at {dir_path}")
        logging.info(f"the directory is created at {dir_path}")

def save_local_df(data, data_path, index=False):
    data.to_csv(data_path, index=index)
    print(f"data frame save at {data_path}")

def get_df(path_to_data: str, sep: str="\t") -> pd.DataFrame:
    df = pd.read_csv(
        path_to_data,
        encoding="utf-8",
        header=None,
        delimiter=sep,
        names=["id", "label", "text"],
    )
    logging.info(f"The input data frame {path_to_data} size is {df.shape}\n")
    return df