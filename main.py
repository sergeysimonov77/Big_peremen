# pip install sklearn
# pip install pandas
# pip install flask

from flask import Flask, request, render_template


app = Flask(__name__)





@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Симонов Виталий Большая перемена</title>
    <style>
        body {
         background:rgba(9, 228, 228, 0.541);
        }
       </style>
</head>
<body>
    <center><h1>Проект Коллективизация 2.0</h1>
    <p>Данный проект создан в рамках конкурса "Большая перемена"
        <br> Симонов Виталий МАОУ "СОШ №13 с УИОП" 8М город Электросталь Московской области
    </p>
    <form action="" method="post">
    <h2>Введите название коллектива</h2>
    <input type="text" name='jj'>
    <button>Отправить</button></center>
    </form>
</body>
</html>
    '''



if __name__ == '__main__':
    app.run(debug=True)