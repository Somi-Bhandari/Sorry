from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Sorry Princess</title>

<style>

body{
background:#0f172a;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
flex-direction:column;
font-family:Arial;
color:white;
}

h1{
font-size:40px;
margin-bottom:40px;
color:#ff4d6d;
}

.heart{
font-size:70px;
margin-bottom:30px;
}

.circle{
position:relative;
width:250px;
height:250px;
animation:spin 10s linear infinite;
}

.circle span{
position:absolute;
left:50%;
top:50%;
transform-origin:0 120px;
font-size:26px;
color:#ff4d6d;
}

@keyframes spin{
100%{
transform:rotate(360deg);
}
}

</style>

</head>

<body>

<h1>For Princess</h1>

<div class="heart">❤️</div>

<div class="circle">
<span style="transform:rotate(0deg)">S</span>
<span style="transform:rotate(45deg)">O</span>
<span style="transform:rotate(90deg)">R</span>
<span style="transform:rotate(135deg)">R</span>
<span style="transform:rotate(180deg)">Y</span>
<span style="transform:rotate(225deg)">❤️</span>
<span style="transform:rotate(270deg)">S</span>
<span style="transform:rotate(315deg)">O</span>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

app.run(debug=True)
