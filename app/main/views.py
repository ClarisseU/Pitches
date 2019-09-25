# from flask import render_template
from app import app
from flask import render_template,request,redirect,url_for, abort
from .forms import UpdateProfile,PitForm,CommentForm
from flask_login import login_required
from ..models import Pitch,User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    categorii=Category.query.all()
    return render_template('index.html', category=categorii)
#views
@main.route('/user/<uname>')
def profile(uname):
    '''
    a function to hold profile
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#adding a new pitch
@main.route('/categories/view_pitch/add/<int:id>', methods=['GET','POST'])
@login_required
def nu_pitch(id):
    '''
    function to insert or add new pitches and fetch from them some data
    '''
    form = PitForm()
    category = Category.query.filter_by(id=id).first()
    title=f'Welcome To Pitches'
    
    if category is None:
        abort(404)
        
    if form.validate_on_submit():
        content = form.content.data
        nu_pitch= Pitch(content=content,category=category.id,user_id=current_user.id,upvotes=0,downvotes=0)
        nu_pitch.save_pitch()
        return redirect(url_for('.index',id=category.id))
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

#viewing a Pitch with its comments
@main.route('/categories/view_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def viewing_pitch(id):
    '''
    a function to view inserted pitches
    '''
    print(id)
    
    pitchez=Pitch.get_pitches(id)
    
    if pitchez is None:
        abort(404)
    comment =Comments.get_comments(id)
    
    return render_template('pitch.html',comment=comment, pitchez=pitchez,category_id=id)

#UPVOTES AND DOWNVOTES
@main.route('/downvote/<int:id>',methods = ['GET','POST'])
def downvotes(id):
    '''
    a function to determine and save downvotes of a pitch
    '''

    pitch = Pitch.query.filter_by(id=id).first()
    pitch.downvotes = pitch.downvotes + 1
    db.session.add(pitch)
    db.session.commit()
    return redirect("/".format(id=pitch.id))


@main.route('/upvote/<int:id>',methods = ['GET','POST'])
def upvotes(id):
    '''
    function to check and save upvotes
    '''
    pitch = Pitch.query.filter_by(id=id).first()
    pitch.upvotes = pitch.upvotes +1
    db.session.add(pitch)
    db.session.commit()
    return redirect("/".format(id=pitch.id))
    return redirect(".profile".format(id=pitch.id))