from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            input {{
                display: block;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot">
                Rotate by:
            </label>
            <input type="number" name="rot" id="rot" value="0">
            <label>
                Message to encode:
            </label>
            <textarea name="text"></textarea>
            <input type="submit">
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    rot = int(rot)
    message = request.form["text"]

    encrypted_message = rotate_string(message, rot)
    return "<h1>" + encrypted_message + "</h1>"




app.run()