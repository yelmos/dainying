from app.exts import db


class Wheel(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    img = db.Column(db.String(100))



class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    name = db.Column(db.String(40))
    # 密码
    password = db.Column(db.String(256))
    # 邮箱
    email = db.Column(db.String(20), unique=True)

    # 令牌
    token = db.Column(db.String(256))

    icon = db.Column(db.String(256),default='head.png')





class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer)
    title = db.Column(db.String(250))
    image = db.Column(db.String(250))
    duration = db.Column(db.Integer)
    request_url = db.Column(db.String(500))




