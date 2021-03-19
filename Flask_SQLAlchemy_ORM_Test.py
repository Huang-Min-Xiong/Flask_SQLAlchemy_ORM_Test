import json
from flask import Flask, render_template, request,Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__) #創建一個Flask物件

# MySql datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/flask_orm_test"
db = SQLAlchemy(app)

# 模型( model )定義
class Product(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, name, price, img, description, state):
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.state = state


#函式的裝飾器:以函式為基礎，提供附加的功能
@app.route('/')
def index():
    # Create data
    db.create_all()
    return '已成功連接資料庫，並且建立表單!'


@app.route('/create')
def create():
    # Add List data
    p1 = Product('Isacc', 8888, 'https://picsum.photos/id/1047/1200/600', '', '')
    p2 = Product('Dennis', 9999,'https://picsum.photos/id/1049/1200/600', '', '')
    p3 = Product('Joey', 7777, 'https://picsum.photos/id/1033/1200/600', '', '')
    p4 = Product('Fergus', 6666,'https://picsum.photos/id/1041/1200/600', '', '')
    p5 = Product('Max', 5555, 'https://picsum.photos/id/1070/1200/600', '', '')
    p6 = Product('Jerry', 4444, 'https://picsum.photos/id/1044/1200/600', '', '')
    p = [p1, p2, p3, p4, p5, p6]

    db.session.add_all(p)
    db.session.commit()
    return '新增資料成功!'
    

@app.route('/read')
def read():
    # 可以用動態參數傳入
    #filters = {'name': 'Isacc'}
    #query = Product.query.filter_by(**filters).first()    

    #查詢多筆資料
    query = Product.query.all()
    dic = {}
    for data in query:
        dic[data.name] = data.price
    return Response(json.dumps(dic), mimetype='application/json') 


@app.route('/delete')
def delete():
    query = Product.query.filter_by(name='Max').first()
    db.session.delete(query)
    db.session.commit()
    return '刪除資料成功!'


@app.route('/update')
def update():
    query = Product.query.filter_by(name='Jerry').first()
    query.price = 1111
    db.session.commit()
    return '更新資料成功!'


if __name__=="__main__":
    app.run(debug=True) 