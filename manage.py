from app import db,create_app
from flask_script import Manager,Server
from app.models import User,Category,Pitch,Comments

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Category = Category,Pitch = Pitch,Comment = Comment)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manage.run()