from django.shortcuts import render
from django.http import HttpResponse
def members(request):
    return HttpResponse(
        
'''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shapes Game</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="main">
        <div id="rect1">
            <div id = "box1" class="class"><h3>1</h3></div>
            <div id = "box2" class="class"><h3>3</h3></div>
        </div>  
        <div id="rect2">
            <div id = "box3" class="class"><h3>2</h3></div>
            <div id = "box4" class="class"><h3>4</h3></div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>''')
# Create your views here.
