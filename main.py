from duckdb_client import DuckDBClient
from config import Config

config = Config()
client = DuckDBClient()
client.add_s3_support(
    region=config.s3.region,
    access_key_id=config.s3.access_key_id,
    secret_access_key=config.s3.secret_access_key,
)

print(
    client.query(
        f"SELECT * FROM read_parquet('s3://{config.s3.bucket_name}/raw/collects/*.parquet');"
    ).fetchall()
)
