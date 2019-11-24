#!python

print("Content-Type: text/html; charset=utf-8")
print()

import cgi
form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello web'

print('''<!DOCTYPE html>
<html>
<head>
    <title>Index</title>
</head>
<body>
    <h1>{title}</h1>
    <ul>
        <li><a href="index.py?id=A">Go to A</a></li>
        <li><a href="index.py?id=B">Go to B</a></li>
        <li><a href="index.py?id=C">Go to C</a></li>
        <li><a href="index.py?id=D">Go to D</a></li>
    </ul>
    <p>
        {desc}
    </p>
</body>
</html>
'''.format(title=pageId, desc=description))