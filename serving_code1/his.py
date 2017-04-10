import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if len(sys.argv) != 3:
    print('usage: python finalresults.py number1,number2')

number1 = sys.argv[1]
number2 = sys.argv[2]

conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor 
cur = conn.cursor()

# get data from Tweetwordcount table   
cur.execute("SELECT db_word, count FROM Tweetwordcount WHERE count>= %s and count <=%s", (number1,number2) )

records = cur.fetchall()
for rec in records:
    print(rec[0], rec[1] )

print("results shows above")
#Closing cursor and connection
cur.close()
conn.close()
