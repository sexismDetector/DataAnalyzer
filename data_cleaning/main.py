
import re

from  PostgreSQLConnector import PostgresConnector




def remove_user_mention(line):
    return re.compile('#\w+ ').sub('', re.compile('RT @\w+: ').sub('', line, count=1)).strip()

def main():


    postgres = PostgresConnector()

    connObj = postgres.connect()
    cur = connObj.cursor()

    print("Type your query")

    user_query = input()


    #print(user_query)

    cur.execute( user_query )

    # show the results of the query
    for row in cur:
        #print(type(row))
        print(row[1].strip("RT "))

    cur.close()


main()
