#!C:\\Users\\PRITHAM\\anaconda3\\python.exe


print("Content-type:text/html; charset=utf-8\n\n")

import cgitb,cgi
import MySQLdb
cgitb.enable()

form = cgi.FieldStorage()
fname = form.getvalue("fn")

connection = MySQLdb.connect('localhost' , 'root' , '' , 'mycgi')
cursor = connection.cursor()
cursor.execute("DELETE FROM tblemp WHERE fname = '%s'"%(fname))
print("<h2>Deleted Succesfullly!!! congo bro</h2>")
print("<style>body{background:url('https://img.freepik.com/free-vector/office-background-video-conferencing_23-2148641674.jpg?w=2000') ;}h2{margin-top: 250px;text-align:center;font-size:80px;letter-spacing:5px;}</style>")
connection.commit()
connection.close()

