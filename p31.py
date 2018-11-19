#!/usr/bin/python3
# p31.py
# Write a CGI script to demonstrate the concept of check button.

import cgi, cgitb
form = cgi.FieldStorage()
if form.getvalue('maths'):
	math_flag = "ON"
else:
	math_flag = "OFF"
if form.getvalue('physics'):
	physics_flag = "ON"
else:
	physics_flag = "OFF"

print ("Content-type:text/html")
print()
print ("<html>")
print ("<head>")
print ("<title>Checkbox -CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> CheckBox Maths is : %s</h2>" % math_flag)
print ("<h2> CheckBox Physics is : %s</h2>" % physics_flag)
print ("</body>")
print ("</html>")

#############################################
