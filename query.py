import duckdb

print("Connecting to MinIO via DuckDB...")

con = duckdb.connect()

con.execute("""
SET s3_region='us-east-1';
SET s3_endpoint='http://localhost:9000';
SET s3_access_key_id='minioadmin';
SET s3_secret_access_key='minioadmin123';
SET s3_use_ssl=0;
SET s3_url_style='path';
""")

df = con.execute("""
    SELECT *
    FROM read_csv_auto('s3://datalake/sales.csv');
""").df()

print(df)
