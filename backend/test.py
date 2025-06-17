from sqlalchemy import create_engine

url = "postgresql://postgres:postgres@localhost:5432/helpdesk"
engine = create_engine(url)
conn = engine.connect()
print("Conexión exitosa")
conn.close()
