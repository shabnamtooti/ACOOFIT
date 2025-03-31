from flask import Flask, render_template, request, url_for, session, redirect
app=Flask(__name__)
app.secret_key='your_secret_key'
app.config['SESSION_TYPE']='filesystem'
#داده های نمومه برای فروشگاه
products=[
    {'name':'Sporting Goods','price':'50/000/000 Rs','image':'images/products1.jpg','Description':'Everywhere'},
    {'name':'Sports Supplement','price':'500/000 Rs','image':'images/products2.jpg','Description':'People over 18 years of age'},
]
comments=[]
ratings=[]
users=[]
cart=[]
@app.route('/products',methods=['GET'])
def products_view():
    return render_template('index.html',products=products)
@app.route('/',methods=['GET'])
def index():
    search_query=request.args.get('query', '')
    filtered_product=[
        p for p in products if search_query.lower()in p['name'].lower()]
    return render_template('index.html',products=filtered_product,comments=comments)
@app.route('/search',methods=['GET'])
def search():
    query=request.args.get('query')   # گرفتن مقدار جستجو شده
    filtered_products=[
        p for p in products if query.lower()in p['name'].lower()]
    return render_template('index.html',query=query,products=filtered_products)
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username not in users:
            users[username]=password
            return redirect(url_for("login"))
        return render_template('register.html')
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username in users and users[username]==password:
            session['username']=username
            return redirect(url_for("index"))
        return render_template("login.html")
@app.route('/add_comment',methods=['POST'])
def add_comment():
    comment_text=request.form['comment']
    comments.append(comment_text)
    return redirect(url_for('index'))
@app.route('/rate',methods=["POST"])
def rate():
    rating=request.form['rating']
    rating.append(int(rating))
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(host="" , debug=True)