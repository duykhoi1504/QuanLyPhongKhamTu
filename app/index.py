import math

from flask import render_template, request, redirect, session, jsonify
import dao, utils
from app import app, login
from flask_login import login_user


@app.route("/")
def index():
    kw = request.args.get('kw')
    page = request.args.get('page')
    cates = dao.load_categories()

    products=dao.load_products(kw=kw,page=page)

    total = dao.count_product()

    return render_template("index.html",

                           products=products,
                           pages=math.ceil(total / app.config['PAGE_SIZE'])                           )


@app.route("/products/<id>")
def details(id):
    return render_template('details.html', id=id)


@app.route('/login',methods=['post', 'get'])
def login_user_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

        next = request.args.get('next')
        return  redirect('/' if next is None else next)
    return render_template('login.html')


@app.route("/admin/login", methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@app.route('/api/cart', methods=['post'])
def add_cart():
    cart = session.get('cart')
    if cart is None:
        cart = {}
    data = request.json
    id = str(data.get("id"))

    if id in cart:  # san pham da co trong gio
        cart[id]["quantity"] = cart[id]["quantity"]+1
    else:  # san pham chua co trong gio
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }
    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/cart')
def cart_list():
    return render_template('cart.html')




@app.context_processor#trang nao cung se co du lieu nay`
def common_resp():
    return{
        'caregories': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)