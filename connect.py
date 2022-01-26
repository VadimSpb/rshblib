import cx_Oracle
import rshblib._cftf02 as config
import pandas as pd

def cft_execute(query) -> pd.DataFrame:
    """
        Return SQL-request as pd.DataFrame or empty dataframe.
        :param query:  SQL query.
        :return: pd.Dataframe
    """
    connection = None
    df = pd.DataFrame()
    
    try:
        connection = cx_Oracle.connect(user=config.username, 
                                   password=config.password,
                                   dsn=config.dsn)
        df = pd.read_sql(query, connection)
    except cx_Oracle.Error as error:
        print(error)
    finally:
        # release the connection
        if connection:
            connection.close()
        return df