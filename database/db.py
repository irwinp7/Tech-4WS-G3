import pymysql 

end_point = "dbmysqlpr.c3cuoeyaoo1i.us-west-1.rds.amazonaws.com"
user = "techg4ws"
passd = "Tech3Cl0ud4W5"

pymysql.connect(
    host=end_point,
    user=user,
    password=passd,
)

print ("Succesfull connection to a database")