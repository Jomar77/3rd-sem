import webbrowser


f = open('DEMO.html', 'w')

message = """<html>
<title>My first HTML</title>
<h1>Welcome to My First HTML Program Using Python</h1>
<h2> My Name is Jomar A. Nacorda</h2>
<body><p>Thank you!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('DEMO.html')