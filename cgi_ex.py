import cgi
form = cgi.FieldStorage()
if not (form.has_key("name") and form.has_key("age")):
    print("<H1>Name & Age not Entered</H1>")
    print("Fill the name and age accurately:")
#return
print("<p>name:", form["name"].value)
print("<p>Age:", form["age"].value)
