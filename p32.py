#!/usr/bin/python3
# p31.py
# Write a CGI script to demonstrate the concept of radio button.

import cgi, cgitb
form = cgi.FieldStorage()
if form.getvalue('subject'):
	subject = form.getvalue('subject')
else:
	subject = "Not set"

print ("Content-type:text/html")
print()
print ("<html>")
print ("<head>")
print ("<title>Radio-CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> Selected Subject is %s</h2>" % subject)
print ("</body>")
print ("</html>")

#############################################
