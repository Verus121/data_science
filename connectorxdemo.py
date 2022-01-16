from dataprep.connector import connect
import asyncio

conn = connect("dblp")
df = asyncio.run(conn.query("publication", q="CVPR 2020"))
print(df)