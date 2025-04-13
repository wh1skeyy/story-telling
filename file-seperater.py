import pandas as pd
data = 'cleaned-data.csv'
data = pd.read_csv(data)

ml_engineer_df = data[data['Q5'] == 'Machine Learning Engineer']
ml_engineer_df.to_csv('machine_learning_engineers.csv', index=False)

dba_df = data[data['Q5'] == 'DBA/Database Engineer']
dba_df.to_csv('dba_database_engineers.csv', index=False)