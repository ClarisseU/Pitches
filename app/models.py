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
        
            
            
        