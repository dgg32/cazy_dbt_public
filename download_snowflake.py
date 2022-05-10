import snowflake.connector
import pandas as pd
import sys

family = sys.argv[1]


con = snowflake.connector.connect(
    user='dbt',
    password='dbtPassword123',
    account='your_snowflake_account_name',
    database='cazy',
    warehouse='COMPUTE_WH',
    role='transform',
    schema='dev'
    )

cur = con.cursor()

sql  = f'select * from {family}_TAXID'

cur.execute(sql)

df = cur.fetch_pandas_all()

df.to_csv(f'{family}.tsv', index=False, sep="\t")