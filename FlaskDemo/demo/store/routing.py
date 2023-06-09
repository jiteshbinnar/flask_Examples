from flask_login import login_user,logout_user,login_required,current_user
from store import app, db
from flask import flash, redirect, render_template, request, url_for,get_flashed_messages
from store.forms import LoginForm, PurchaseItem, RegisterForm, SellItem
from store.models import Item,User

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/store",methods=["POST","GET"])
@login_required
def store():
    purchase_form=PurchaseItem()
    sell_form=SellItem()
    #for purchase items
    if request.method=="POST":
        purchase_item=request.form.get('purchase_item')
        purchase_obj=Item.query.filter_by(pname=purchase_item).first()
        if purchase_obj:
            purchase_obj.buy(current_user)
            flash(f"Congratulations..! You purchased {purchase_obj.pname} at price {purchase_obj.price}",category='success')
    
    #for sell items

    if request.method=="POST":
        sell_item=request.form.get('sell_item')
        sell_obj=Item.query.filter_by(pname=sell_item).first()
        if sell_obj:
            sell_obj.sell()
            flash(f"Congratulations..! You sold {sell_obj.pname} at price {sell_obj.price}",category='success')




        return redirect(url_for('store'))
    # u1=User(username='jjj',email_address='jjj@gmail.com',password_hash='1234')
    # db.session.add(u1)
    # # db.session.commit()
    # u1=User.query.all()
    # item1=Item(pname='gloves',price=900)
    if request.method=="GET":
        items1=Item.query.filter_by(owner=None)
        own_items=Item.query.filter_by(owner=current_user.id)
    # item1.owener= User.query.filter_by(username='jjj').first()
    # print(item1)
        return render_template("store.html",items=items1, purchase_form=purchase_form, own_items=own_items, sell_form=sell_form)


@app.route("/register", methods=['POST','GET'])
def register_form():
    form=RegisterForm()
    if form.validate_on_submit():
        create_user=User(username=form.username.data,
                        email_address=form.email.data,
                        password=form.password1.data)

        db.session.add(create_user)
        db.session.commit()
        login_user(create_user)
        flash(f"Success..! You are login as: {create_user.username}", category='success')
        return redirect(url_for('store'))
    
    if form.errors != {}:
        for error_catch in form.errors.values():

            flash(f"The errors catch during register forms are: {error_catch}", category='danger')

    return render_template("register.html", form=form)    

@app.route("/login_page",methods=['POST', 'GET'])
def login_form():
    form=LoginForm() 
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password1.data):
            login_user(attempted_user)
            flash(f"Success..! You are login as: {attempted_user.username}", category='success')
            return redirect(url_for('store'))
           
        else:
            flash(f"Oops..! Entered credentials are wrong, Please Try again",category='danger')

    return render_template("login.html",form=form)

@app.route("/logout")
def logout_form():
    logout_user()
    flash(f"User log out successfully..!",category='info')
    return redirect(url_for('home_page'))


