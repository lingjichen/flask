from flask import Blueprint

main = Blueprint('main', __name__)

#注册路由的程序在views中，错误处理程序在errors中，在末尾导入避免循环导入依赖
from . import views, errors
