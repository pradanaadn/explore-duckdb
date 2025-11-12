import duckdb

query = """
SELECT *
FROM 'datasets/flights-1m.parquet';
"""
con = duckdb.connect()
df = con.execute(query).fetchdf()
print(df)
