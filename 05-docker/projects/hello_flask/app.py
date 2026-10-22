from flask import Flask



app = Flask(__name__)

@app.route('/')
def hello_world():
    return"""
    <body style="background-color: lightblue; text-align: center; font-family: Courier New;">
      <h1>Hello there! I'm Roshaan</h1>
      <p> Welcome to my first dockerised application </p>
      <p><a href= "https://www.linkedin.com/in/r-ashfaq">
      My Linkedin</a></p>
      </body>
"""


if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)