import pandas as pd

__all__ = [
    "separate_roles",]

def separate_roles(input_file):
    data = pd.read_csv(input_file)

    ml_engineer_df = data[data['Q5'] == 'Machine Learning Engineer']
    ml_engineer_df.to_csv('machine_learning_engineers.csv', index=False)

