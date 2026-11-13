from flask import Flask, request, render_template_string

app = Flask(__name__)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Special Message</title>
</head>
<body style="text-align:center; font-family:sans-serif; margin-top:100px; padding:20px;">
  <h2>💌 Apnar Jonno Ekti Special Message</h2>
  <form method="POST">
    <input type="text" name="user_name" placeholder="Apnar nam ba entry likhun..." required style="padding:10px; font-size:16px; border-radius:5px; border:1px solid #ccc;">
    <button type="submit" style="padding:10px 20px; font-size:16px; background-color:#28a745; color:white; border:none; border-radius:5px; cursor:pointer;">Submit</button>
  </form>
  {% if message %}
    <h3 style="color:blue; margin-top:25px; line-height: 1.5;">{{ message | safe }}</h3>
  {% endif %}
</body>
</html>
"""
name = input("enter your name: ")

if name == "jim":
    print(f"{name} chutiya sala")
elif name == "ainan":
    print(f"{name} behen chod sala")
elif name == "mourin":
    print(f"{name} next dhoa special adda when?")
elif name == "afif":
    print(f"{name} chol jersey banai")
elif name == "jarin":
    print(f"{name} seiiii note koris thanksss")
elif name == "shoroni":
    print(f"{name} doi kobe khabo")
elif name == "swarna":
    print(f"{name} our only baddie")
elif name == "daita":
    print(f"{name} class kor sala")
elif name == "maisha":
    print(f"{name} depression ses kobe?")
else:
    print("no message found")


    
