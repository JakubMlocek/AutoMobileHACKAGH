from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:postgres@138.3.243.190:5432/mydb')

df = pd.read_sql_query('SELECT * FROM cars WHERE id = 1', engine)

engine.dispose()

df.to_csv('script_data.csv', index=False)