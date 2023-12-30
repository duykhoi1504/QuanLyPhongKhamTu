from flask import render_template,request

from app import app
import dao

@app.route("/")
def index():
    kw=request.args.get('kw')

    cates=dao.load_categories()
    products=dao.load_products(kw=kw)
    return render_template("index.html",categories=cates,products=products)

@app.route("/products/<id>")
def details(id):
    return render_template('details.html',id=id)



if __name__=='__main__':
    app.run(debug=True)