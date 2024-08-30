from flask import Blueprint, request, jsonify
from services.user import user_login, user_register, user_edit, user_delete, user_charge

# 创建用户蓝图，用于处理与用户相关的路由
user = Blueprint('user', __name__)

# 登录路由
@user.route('/login', methods=['POST'])
def login():
    data = request.form
    if not data:
        return jsonify({
            'code': -4,
            'message': '无效输入',
            'data': None
        })

    username = data.get('username')
    password = data.get('password')

    # 检查必填字段
    if not username or not password:
        return jsonify({
            'code': -4,
            'message': '用户名和密码为必填项',
            'data': None
        })

    # 调用用户登录服务
    return user_login(username, password)

# 注册路由
@user.route('/register', methods=['POST'])
def register():
    data = request.form
    if not data:
        return jsonify({
            'code': -4,
            'message': '无效输入',
            'data': None
        })

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # 检查必填字段
    if not email or not username or not password:
        return jsonify({
            'code': -4,
            'message': '所有字段均为必填项',
            'data': None
        })

    # 调用用户注册服务
    return user_register(email, username, password)

# 编辑用户信息路由
@user.route('/edit', methods=['PUT'])
def edit():
    data = request.form
    if not data:
        return jsonify({
            'code': -4,
            'message': '无效输入',
            'data': None
        })

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    avatar = data.get('avatar')
    nickname = data.get('nickname')

    # 用户名是必填字段
    if not username:
        return jsonify({
            'code': -4,
            'message': '用户名为必填项',
            'data': None
        })

    # 调用用户信息编辑服务
    return user_edit(email, username, password, avatar, nickname)

# 删除用户路由
@user.route('/delete', methods=['DELETE'])
def delete():
    data = request.form
    if not data:
        return jsonify({
            'code': -4,
            'message': '无效输入',
            'data': None
        })

    username = data.get('username')
    password = data.get('password')

    # 检查必填字段
    if not username or not password:
        return jsonify({
            'code': -4,
            'message': '用户名和密码为必填项',
            'data': None
        })

    # 调用用户删除服务
    return user_delete(username, password)

# 用户充值路由
@user.route('/charge', methods=['POST'])
def charge():
    data = request.form
    if not data:
        return jsonify({
            'code': -4,
            'message': '无效输入',
            'data': None
        })

    username = data.get('username')
    balance = data.get('balance')

    # 检查必填字段
    if not username or not balance:
        return jsonify({
            'code': -4,
            'message': '用户名和余额为必填项',
            'data': None
        })

    # 调用用户充值服务
    return user_charge(username, balance)
