

from  PostgreSQLConnector import PostgresConnector

def Data_Query(user_query):

    postgres = PostgresConnector()

    connObj = postgres.connect()
    cur = connObj.cursor()


    cur.execute( user_query )
    
    x = []

    # show the results of the query
    for row in cur:
        #print(type(row))
        
        x.append( row[1].strip("RT ") )
        #print(x)
        
    

    cur.close()
    
    return x


#Library to use regular expressions to remove URLS in data set
import re
import pickle




#%%capture
nonsexist_tweets = Data_Query("SELECT * FROM \"Tweets\" where label = 'none' ")

for e in range(len(nonsexist_tweets)):
  nonsexist_tweets[e] = result = re.sub(r"http\S+", "", nonsexist_tweets[e])

file1 = open('nonsexist_tweets', 'wb')

pickle.dump(nonsexist_tweets,file1)
file1.close()

#####

sexist_tweets = Data_Query("SELECT * FROM \"Tweets\" where label = 'sexist' ")

for e in range(len(nonsexist_tweets)):
  sexist_tweets[e] = result = re.sub(r"http\S+", "", sexist_tweets[e])


file1 = open('sexist_tweets', 'wb')

pickle.dump(sexist_tweets,file1)
file1.close()

"""

infile = open('nonsexist_tweets','rb')
nonsexist_tweets = pickle.load(infile)
infile.close()


infile = open('sexist_tweets','rb')
sexist_tweets = pickle.load(infile)
infile.close()

"""