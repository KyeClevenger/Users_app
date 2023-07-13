from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_model import User




@app.route('/')
@app.route('/users')
def all_users():
    all_users = User.get_all()
    return render_template('index.html', all_users=all_users)


@app.route('/users/new')
def new_user():
    return render_template("user_new.html")


@app.route('/users/create', methods=['POST'])
def create_user():
    print("Request form", request.form)
    User.create(request.form)
    return redirect('/users')

@app.route('/users/<int:id>/view')
def view_one_user(id):
    data = {
        'id': id
    }
    one_user = User.get_one(data)
    return render_template("user_one.html", one_user=one_user)

@app.route('/users/<int:id>/edit')
def edit_user_form(id):
    data = {
        'id': id
    }
    one_user = User.get_one(data)
    return render_template("user_edit.html",one_user=one_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    data = {
        **request.form,
        'id':id
    }
    User.update(data)
    return redirect('/')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
            'id': id
        }
    User.delete(data)
    return redirect('/')