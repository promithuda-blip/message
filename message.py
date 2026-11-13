from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Special Message</title>
</head>
<body style="text-align:center; font-family:sans-serif; margin-top:80px; padding:20px; background-color: #f9f9f9;">
  <div style="max-width: 500px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
    <h2>💌 Batch Special Message</h2>
    <form method="POST" style="margin-top: 20px;">
      <input type="text" name="user_name" placeholder="Apnar nam likhun..." required style="padding:12px; font-size:16px; width: 80%; border-radius:5px; border:1px solid #ccc; outline: none;">
      <br><br>
      <button type="submit" style="padding:12px 25px; font-size:16px; background-color:#28a745; color:white; border:none; border-radius:5px; cursor:pointer;">Submit</button>
    </form>
    {% if message %}
      <h3 style="color:#333; margin-top:30px; line-height: 1.5; background: #eef9ff; padding: 15px; border-radius: 5px;">{{ message }}</h3>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    msg = ""
    if request.method == "POST":
        # input-take lowercase kore niye check korbe jate boro/choto hater lekhar problem na hoy
        name = request.form.get("user_name", "").strip().lower()
        
        # Apnar original logic-ti ekhane bosano holo:
        if name == "jim":
            msg = f"{name} chutiya sala"
        elif name == "ainan":
            msg = f"{name} behen chod sala"
        elif name == "mourin":
            msg = f"{name} next dhoa special adda when?"
        elif name == "afif":
            msg = f"{name} chol jersey banai"
        elif name == "jarin":
            msg = f"{name} seiiii note koris thanksss"
        elif name == "shoroni":
            msg = f"{name} doi kobe khabo"
        elif name == "swarna":
            msg = f"{name} our only baddie"
        elif name == "daita":
            msg = f"{name} class kor sala"
        elif name == "maisha":
            msg = f"{name} depression ses kobe?"
        else:
            msg = "no message found"
            
    return render_template_string(HTML_PAGE, message=msg)

if __name__ == "__main__":
    app.run()
