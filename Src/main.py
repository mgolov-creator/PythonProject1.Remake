from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False) #string up to 250 symbols
    price = db.Column(db.Integer, nullable = False)
    isActive = db.Column(db.Boolean, default = True)
    description = db.Column(db.Text, nullable = False)
    def __repr__(self):
        return self.title


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False) #email
    Surname = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Money = 0
    def __repr__(self):
        return str(self.Name) + "%" + str(self.Password)


@app.route('/deleteaccount')
def deleteaccount():
    global UserStatus
    try:
        i = User.query.filter((User.Name) == UserStatus.user.Name)
        print(*i, end = " ")
        db.session.delete(*i)
        db.session.commit()
        print("removed")
        UserStatus = CurrentUserStatus(False, User())
    except:
        pass
    return redirect('/')


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', items = items, UserStatus = UserStatus)


@app.route('/errors')
def errors():
    return render_template('errors.html', UserStatus = UserStatus)


@app.route('/about')
def about():
    return render_template('about.html', UserStatus = UserStatus)


@app.route('/buy/<int:id>')
def item_buy(id):
    if UserStatus.IsValid():
        UserStatus.error = "Пока что нет возможности купить этот товар, потому что платежные системы в России не работают :("
        return redirect('/errors')
    UserStatus.error = "Авторизируйтесь, чтобы купить продукт"
    return redirect('/errors')


@app.route('/additem', methods=['POST', 'GET'])
def additem():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        description = request.form['description']
        item = Item(title = title, price = price, description = description)
        if (not UserStatus.IsValid()):
            UserStatus.error = "Чтобы добавить товар нужно авторизироваться"
            return redirect('/errors')
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            UserStatus.error = "К сожалению, возникла ошибка"
            return redirect('/errors')
    else:
        return render_template('additem.html', UserStatus=UserStatus)



@app.route('/accountinfo')
def accountinfo():
    if (not UserStatus.IsValid()):
        UserStatus.error = "Чтобы посмотреть аккаунт нужно авторизироваться"
        return redirect('/errors')
    else:
        return render_template('accountinfo.html', UserStatus = UserStatus)


@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        Name = request.form['Name']
        Surname = request.form['Surname']
        Password = request.form['Password']
        user = User(Name = Name, Surname = Surname, Password=Password)
        for i in Password:
            if not(i.isalpha() or i.isdigit()):
                UserStatus.error = "пароль может содержать только буквы и цифры"
                return redirect('/errors')
        try:
            users = User.query.all()
            for i in users:
                if str(str(i).split("%")[0]) == str(user.Name):
                    UserStatus.error = "К сожалению, пользователь с таким именем уже существует"
                    return redirect('/errors')
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            UserStatus.error = "К сожалению, возникла ошибка"
            return redirect('/errors')
    else:
        return render_template('adduser.html')


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    global UserStatus
    if request.method == 'POST':
        try:
            Name = request.form['Name']
            Password = request.form['Password']
            user = User(Name = Name, Password=Password)
            try:
                users = User.query.all()
                if users ==[]:
                    UserStatus.error = "На текущий момент в магазине никто не зарегистрировался. Будьте первым посетителем!"
                    return redirect('/errors')
                for i in users:
                    if str(str(i).split("%")[0]) == str(user.Name):
                        if str(user.Password) == str(i).split("%")[1]:
                            UserStatus = CurrentUserStatus(True, user)
                            return redirect('/')
                        else:
                            UserStatus.error="Пароль неправильный"
                            return redirect('/errors')
            except:
                UserStatus.error =  "К сожалению, возникла ошибка"
                return redirect('/errors')
        except:
            UserStatus.error = "На текущий момент в магазине никто не зарегистрировался"
            return redirect('/errors')
    else:
        try:
            return render_template('signin.html')
        except:
            UserStatus.error = "Произошла непредвиденная ошибка. Возможно вам нужно зарегистрироваться"
            return redirect('/errors')


class CurrentUserStatus():
    isautorizated = False
    user = User()
    error = ""
    def __init__(self, isautorizated=False, user=User(), error=""):
        self.isautorizated = isautorizated
        self.user = user
        self.error=error
    def IsValid(self):
        return self.isautorizated
UserStatus = CurrentUserStatus(False, User(), "")



if __name__ == "__main__":
    app.run(port=8001, debug=True) # add debug mode, на стандартном 5000 у меня не работал. При желании можно поменять на 5000
