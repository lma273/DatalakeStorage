import duckdb

print("Reading MinIO CSV via presigned URL...")

PRESIGNED_URL = "http://localhost:9000/datalake/sales.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minioadmin%2F20251125%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251125T164317Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=95e7021a659c0cca64887d42ca783352ea3ad5c45e3e143692e5aea792f19271"

con = duckdb.connect()

df = con.execute(f"""
    SELECT *
    FROM read_csv_auto('{PRESIGNED_URL}');
""").df()

print(df)
