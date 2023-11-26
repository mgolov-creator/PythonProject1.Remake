Эта программа - виртуальный магазин.

Для запуска программы нужно:
1) установить необходимые библиотеки из requiremnets.txt
2) "активировать" базу данных. У меня в PyCharm для этого нужно написать в терминале:
python
from main import app
from flask import Flask, request, current_app
app_context=app.app_context()
app_context.push()
from main import db
db.create_all()
exit()

Функционал:
