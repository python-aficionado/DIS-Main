import mysql.connector
import json
import os

credentials = json.load(open("credentials.json"))

cnx = mysql.connector.connect(
    user=credentials["mysql"]["username"],
    password=credentials["mysql"]["password"],
    host="127.0.0.7",
    database="lactapp_dev",
)
cursor = cnx.cursor()

fd = open(os.path.join("data", "reply.sql"), "rb")
sql_file = fd.read().decode('utf-8')
fd.close()
cursor.execute(sql_file, multi=True)
