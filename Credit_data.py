import json
import sqlite3 
import numpy as np


#read file
with open('prequalresult.json') as f:
    data = json.load(f)
data = data[0]

title = list(data.keys())
value = list(data.values())
title1 = list(data[title[-1]].keys())
value1 = list(data[title[-1]].values())
title = title[0:-1]
title.extend(title1)
value = value[0:-1]
value.extend(value1)






#create SQL table
connection = sqlite3.connect("database.db") 
crsr = connection.cursor() 

columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in title)
values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in value)
sql_createTable = """CREATE TABLE mytable(
%s
);""" %(columns)
crsr.execute(sql_createTable) 
sql_insertData = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
crsr.execute(sql_insertData) 

connection.commit() 
connection.close()


