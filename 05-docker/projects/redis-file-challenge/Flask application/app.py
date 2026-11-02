# app.py
import os 
#Download the operating system
from flask import Flask, request 
#Download the flask application
import redis 
#Download the redis database
import urllib.request
import json
#Download the IP 

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int (os.getenv('REDIS_PORT', '6379'))
db = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello_world():
    visitor_ip = request.headers.get("X-Real-IP", request.remote_addr)

    with urllib.request.urlopen(f"http://geoip:8000/{visitor_ip}") as response:
        data = json.load(response)

    country = data.get("country") or "Unknown"
    db.hincrby("country_visits", country, 1)
    country_visits = db.hgetall("country_visits")
    country_list = ""

    for country_name, visits in country_visits.items():
        country_list += f"<p>{country_name.decode()}: {visits.decode()} visits</p>"

    html = """
    


 
<style> 

h1 { 
color: #8B3F25;
text-shadow: 0 0 18px rgba(205, 125, 65, 0.55);
 }


body {
background-color: #F5EDE3;
margin: 0;
background: linear-gradient(to bottom, #F5EDE3, #B7A99C);
}

.container { 
background-color: #FFF8F0;
padding-top: 50px;
padding: 40px 0px;
font-family: arial, sans-serif;
text-align: center;
font-size: 30px;
border-radius: 25px;
min-height: 60vh;
box-shadow: 12px 12px 30px rgba(0, 0, 0, 0.25);
color: #292929;
margin: 50px;
background: linear-gradient(to bottom, #FFFFFF, #D5CEC8);
}




button {
background-color: #BE9568;
color: #FFFFFF;
font-size: 15px;
padding: 15px 30px;
border-radius: 25px;
cursor: pointer;
text-align: center;
margin-top: 65px;
box-shadow: 0px 4px 15px rgba(166, 124, 82, 0.25);
border: none;
}
button:hover {
    box-shadow: 0px 0px 25px 8px #A67C52;
}

    
</style>
<div class="container">
<h1>Welcome to VisitPulse Pro!</h1>
<p>Click to learn more about me or to see how many times this page has been visited!</p>

<a href="/about"><button>About Me</button><a/>
<a href="/count"><button>View Count</button><a/>
</div>
"""
    return html

@app.route('/count')
def visit_count():
    count = db.incr("visits")
   
    country_visits = db.hgetall("country_visits")
    country_list = ""

    for country_name, visits in country_visits.items():
            country_list += f"<div class='country-row'>{country_name.decode()}: {visits.decode()} visits</div>"
    
    html = f"""
     <html>
<head>
    <style>
    body {{ 
        background: linear-gradient(to bottom, #F5EDE3, #B7A99C);
        font-family: Arial, sans-serif;
        text-align: center;
        min-height: 100vh;
}}
    .container {{
        background: linear-gradient(to bottom, #FFFFFF, #D5CEC8);
        padding: 40px;
        margin: 50px auto;
        max-width: 700px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}}
h1 {{
    color: #80502E;
    font-family: Georgia, serif;
}}
p {{
    color: #80502E;
    font-size: 18px;
}}
    .container-row {{
    background: #F2E7DA;
    padding: 12px;
    margin: 8px 0;
    border-radius: 8px;
    color: #80502E;

 }}
nav {{
    background: #F5EDE3;
    padding: 20px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #D5CEC8;
}}
nav a:hover {{
    box-shadow: 0px 0px 25px 8px #A67C52;
    border-radius: 20px;
}}
button:hover {{
    box-shadow: 0px 0px 25px 8px #A67C52;
}}
nav a {{
    color: #80502E;
    text-decoration: none;
    margin-left: 25px;
    font-weight: bold;
}}
 </style>
     
</head>
<body>
<nav>
    <span>VisitPulse Pro</span>
<div>
    <a href="/">Home</a>
    <a href="/about">About</a>
</div>
</nav>
<div class="container">
<h1> The Visit Count </h1>

<p> This is your {count} visit of this page </p>
<h1> Visits by Country </h1> 
{country_list} 
</div>
</body>
</html>
        """
    return html








@app.route('/about')
def about_page():

    return """
    <style>
    body { 
        background: linear-gradient(to bottom, #F5EDE3, #B7A99C);
        font-family: Arial, sans-serif;
        text-align: center;
        min-height: 100vh;
        

}
    .container {
        background: linear-gradient(to bottom, #FFFFFF, #D5CEC8);
        padding: 40px;
        margin: 50px auto;
        max-width: 700px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        
}
h1 {
    color: #80502E;
    font-family: Georgia, serif;
}
p {
    color: #80502E;
    font-size: 18px;
}
nav {
    background: #F5EDE3;
    padding: 20px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #D5CEC8;
}

nav a {
    color: #80502E;
    text-decoration: none;
    margin-left: 25px;
    font-weight: bold;
}
nav a:hover {
    box-shadow: 0px 0px 25px 8px #A67C52;
    border-radius: 20px;
}
button {
    background: #BE9568;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 20px;
    cursor: pointer;
}
button:hover {
    box-shadow: 0px 0px 25px 8px #A67C52;
}
</style>
<body>
<nav>
    <span>VisitPulse Pro</span>
<div>
    <a href="/">Home</a>
    <a href="/count">count</a>
</div>
</nav>
    <div class="container">


<h1>More about who I am</h1> 
<p> I graduated in 2026 and I am now on a journey to develop my tech skills</p>
<h2>My Skills</h2>
<p>Linux | GIT | Networking | Docker | Bash</p>

<a href="https://www.linkedin.com/in/r-ashfaq"><button>My LinkedIn</button></a>
</div>
</body>

"""





@app.route('/GeoIP')
def Location_page():
    visitor_ip = request.headers.get("X-Real-IP", request.remote_addr)
    with urllib.request.urlopen(f"http://geoip:8000/{visitor_ip}") as response:
        data = json.load(response)

    return f"Country: {data['country']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
