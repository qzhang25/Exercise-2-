import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Use psycopg to connect to Postgres

conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

#create a cursor 
cur = conn.cursor()

if len(sys.argv) == 1:
    cur.execute("SELECT db_word, count FROM Tweetwordcount;")
    records = cur.fetchall()
    sorted_records = sorted(records, key = lambda records: records[0])
    print(sorted_records)
    for rec in records:
        print('result')
        print(rec[0], rec[1] )
elif len(sys.argv) == 2:
    word = str(sys.argv[1])
    cur.execute("SELECT db_word , count FROM Tweetwordcount WHERE db_word = %s;", (word,))
    record = cur.fetchone()
    print(record)
else:
    print('usage: python finalresults.py word or python finalresults.py')
    sys.exit(1)

    cur.close()
    conn.close()

