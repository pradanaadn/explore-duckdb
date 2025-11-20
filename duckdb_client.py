import duckdb


class DuckDBClient:
    def __init__(self):
        self.connection = duckdb.connect()

    def add_s3_support(self, region: str, access_key_id: str, secret_access_key: str):
        self.connection.execute("""
        INSTALL httpfs;
        LOAD httpfs;
        """)
        
        self.connection.execute(f"""
            CREATE SECRET (
            TYPE s3,
            KEY_ID '{access_key_id}',
            SECRET '{secret_access_key}',
            REGION '{region}'
            );
            """
        )
        
    def query(self, sql: str):
        return self.connection.execute(sql)
    
    def close(self):
        self.connection.close()
        
        