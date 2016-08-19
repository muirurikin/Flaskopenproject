from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm,RegisterForm
from models import *



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/Users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        # db.session.add(user)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run()