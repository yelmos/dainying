import hashlib
import os
import time
import uuid

from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash

from app.exts import db
from app.models import Wheel, User, Movies

blue = Blueprint('blue',__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def home():
    wheels = Wheel.query.all()

    movies = Movies.query.all()

    token = session.get('token')
    user = None
    if token:
        user = User.query.filter(User.token == token).first()

    return render_template('home.html',wheels=wheels,user=user,movies=movies)


@blue.route('/logined/<int:postid>/')
def logined(postid):
    movies = Movies.query.filter(Movies.postid == postid)

    return render_template('home_logined.html',movies=movies)




@blue.route('/collect/')
def collect():
    return render_template('home_logined_collected.html')



@blue.route('/login/',methods=['POST','GET'])
def login():
    username = request.form.get('username')
    pwd1 = request.form.get('password')



    users = User.query.filter(User.name == username)
    if users.count():
        user = users.first()
        passwd = user.password  # 数据库中加密的密码

        # 更新token
        if check_password_hash(passwd,pwd1):
            user.token = get_token()
            db.session.add(user)
            db.session.commit()
        # 状态保持
            session['token'] = user.token
            return redirect(url_for('blue.home'))
        else:
            return render_template('login.html')

    else:
        return render_template('login.html')

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/img/'
print(BASE_DIR )
@blue.route('/register/',methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form.get('username')
        pwd = request.form.get('password')
        repwd = request.form.get('repassword')
        email = request.form.get('email')






        user = User()
        user.name = name
        user.email = email

        user.password = generate_password_hash(password=pwd)
        imgName = user.name + '.png'
        imagepath = os.path.join(BASE_DIR,imgName)
        icon = request.form.get('icon')
        with open(imagepath,'wb') as fp:
            for data in icon.chunks():
                fp.write(data)


       
        user.icon = imgName



        user.token = get_token()







        if len(name) <=6 or len(name) >= 16 :

            msg = str("请输入6-16位用户名")


            return render_template('register.html',msg=msg)
        elif len(pwd) <= 5:
            msg1 = str("请输入6位以上拼音字母组合密码")
            return render_template('register.html',msg1=msg1)
        elif pwd != repwd :
            msg2 = str("请输入6位以上拼音字母组合密码")
            return render_template('register.html',msg2=msg2)
        else:
            users = User.query.filter(User.name == name)

            if users.count() > 0:
                return render_template('register.html')
            else:


                db.session.add(user)
                db.session.commit()
                session['token'] = user.token



                return redirect(url_for('blue.home'))
    else:
        return render_template('register.html')


@blue.route('/userinfo/')
def userinfo():
    return render_template('userinfo_mod.html')


@blue.route('/logout/')
def logout():
    session.pop('token')

    return redirect(url_for('blue.home'))


# 获取token
def get_token():
    hash = hashlib.sha512()
    hash_str = str(uuid.uuid4()) + str(int(time.time()))
    hash.update(hash_str.encode('utf-8'))
    return hash.hexdigest()


def generate_password(password):
    hash = hashlib.md5()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

