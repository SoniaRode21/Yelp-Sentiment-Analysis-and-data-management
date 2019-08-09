import pandas as pd # pandas is used to read csv files
import MySQLdb # MySQLdb is used to connect Python with MySQL
import csv, sys

csv.field_size_limit(sys.maxsize)

def connect_to_db(host, user, password, database):
	db = MySQLdb.connect(host=host,
    					user=user,
    					passwd=password,
    					db=database)
	db.set_character_set('utf8')
	return db

def parse_db():
	user = pd.read_csv("./data/user.csv", engine='python')
	user = user.drop(['elite','friends'],axis=1)
	user = user.dropna()

	return user

user_db = parse_db()

def create_MySQL_table(db, tableName, dataframe, verbose = False):
    """
    db: MySQLdb connection
    tableName: the name of the table to be created in MySQL
    dataframe: the dataframe read from the .csv file
    verbose: will print the generated sql command if True
    """
    cursor = db.cursor()
   
    # insert the values into the table
    colStr = "" # generate a string of column names separated by ", "
    for colName in dataframe.columns:
        colStr += colName + ","
    colStr = colStr.strip(",")
    for row in dataframe.iterrows():
    	sql = "INSERT INTO " + tableName + " (" + colStr + ") VALUES ("
    	formatStr = ""; valueStr = ""
    	sql += ", ".join(str(row[1].values).strip("[]").split(' ')) + ")"
    	print(sql)
    	cursor.execute(sql) 
    	db.commit()
   

def main():
	host = '35.193.29.72'																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																		
	user = 'unagi'
	password = 'unagi@123'
	database = 'Yelp'
	db = connect_to_db(host, user, password, database)     

	create_MySQL_table(db, "user", user_db, verbose = False)

	cursor = db.cursor()
	cursor.fetchall()

if __name__ == '__main__':
    main()