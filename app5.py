from flask import Flask, render_template, request, redirect, url_for
# app = Flask(__name__)
# @app.route('/')
# def log():
#     return render_template('shoppinglist.html')
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     if username == "Matthew" and password == "1234":
#         return "Welcome %s" % username + request.method
#     else:
#         return "Error in logging in" + request.method
# if __name__ == '__main__':
#     app.run(debug=True)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def shoppinglist():
    if request.method == 'POST':
        item = request.form['item']
        ID = request.form['itemID']
        quantity = request.form['quantity']
        price = request.form['price']
        redirect(url_for('showitem', item=item, ID=ID, quantity=quantity, price=price))
    return render_template('shoppinglist.html')

app.route('/showitems/<string:item>,<string:ID>,<string:quantity>,<string:price>', method=['POST'])
def showitem(item, ID, quantity, price):
    return render_template('showitems.html', item=item, ID=ID, quantity=quantity, price=price)

if __name__ == '__main__':
    app.run(debug=True)
