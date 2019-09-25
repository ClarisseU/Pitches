from . import db

class Pitch:
    '''
    Pitch class to define pitch objects
    '''
    __tablename__='pitch'
    
    id = db.Column(db.Integer,primary_key = True)
    content =  db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    title = db.Column(db.String(255))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    comments = db.relationship('Comment',backref = 'pitches', lazy ="dynamic")
    publishedAt = db.Column(db.DateTime,default=datetime.utcnow)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    
    def save_pitches(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitches.clear()
        
    def get_pitch(id):
        pitch = Pitch.query.filter_by(category=id).all_pitches
        return pitch
    
    @classmethod
    def count_pitches(cls,uname):
           user = User.query.filter_by(username=uname).first()
        pitches = Pitch.query.filter_by(user_id=user.id).all()
        
        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1
            
        return pitches_count
    
     def __repr__(self):
        return f'Pitch {self.id}'
    
    
class Category(db.model):
    __tablename__='category'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'categories', lazy ="dynamic")
    
    def save_cat(self):
        db.session.add(self)
        db.session.commit
        
        
    @classmethod
    def get_catz():
        category = Category.query.all()
        return category    
    
    def __repr__(self):
        return f'Category {self.id}'
    
    
class Comments(db.model):
    __tablename__= 'comments' 
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    def save_comment(self):
        '''
        function to save comments
        '''
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(self, id):
        comment = Comments.query.filter_by(pitchez_id=id).all() 
        return comment 
       
        
            
            
        