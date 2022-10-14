#!C:\\Users\\PRITHAM\\anaconda3\\python.exe


print("Content-type:text/html; charset=utf-8\n\n")

import cgitb,cgi
import MySQLdb
cgitb.enable()

connection = MySQLdb.connect('localhost' , 'root' , '' , 'mycgi')
cursor = connection.cursor()
cursor.execute("select * from tblemp")
print("<html>")
print("<body>")
print("<h1>This is show data page</h1>")
print("<div class='container'>")
print("<font size='5' face='Courier New' >")
print("<table border='1px' width='100%'>")
print("<caption>Employee Details</caption>")
print("<tr><th>First name</th><th>Last name</th></tr>")
for row in cursor.fetchall():
    print("<tr><td>%s</td>"%row[0])
    print("<td>%s</td></tr>"%row[1])
print("</table>")
print("</div>")
print("</body>")
print("<style>tr:nth-child(even) {background-color: #D6EEEE;}h1{text-align:center;}.container{}body{background: url('https://img.freepik.com/free-vector/office-background-video-conferencing_23-2148641674.jpg?w=2000') ;}table td, table th {font-size: 30px;}td {text-align: center;}</style>")
print("</html>")
connection.commit()
connection.close()
	