import PostgreSQLConnector

def Get_Conector_Object():


    postgres = PostgresConnector()

    connObj = postgres.connect()
    cur = connObj.cursor()

    return cur