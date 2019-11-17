#!python

print("Content-Type: text/html; charset=utf-8")
print()

import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print(pageId)

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
    </ul>
    <p>
        This page is {title}
    </p>
</body>
</html>
'''.format(title=pageId))