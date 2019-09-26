from . import auth
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .. import db
from flask_login import login_user,login_required, logout_user
from ..models import User
from .forms import RegistrationForm,LoginForm
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
   '''
   function to login the user
   '''
   form= LoginForm()
   if form.validate_on_submit():
       user=User.query.filter_by(email=form.email.data).first()
       if user is not None and user.verify_password(form.password.data):
           login_user(user,form.remember.data)
           return redirect(request.args.get('next')or url_for('main.index'))
       flash('invalid email or password')
   return render_template('auth/login.html',log=form)


@auth.route('/logout')
@login_required
def logout():
   '''
   function to logout the user
   '''
   logout_user()
   return redirect(url_for("main.index"))

@auth.route('/signup',methods=['GET','POST'])
def signup():
   '''
   function to register a new user
   '''
   form=RegistrationForm()
   if form.validate_on_submit():
       user=User(email=form.email.data, username=form.username.data,password=form.password.data)
       db.session.add(user)
       db.session.commit()
       
       mail_message("Welcome to Pitch","email/welcome_user",user.email,user=user)
       return redirect(url_for('auth.login'))
       title = 'Pitch - New Account'
   return render_template('auth/signup.html',r=form)