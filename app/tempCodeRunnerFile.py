
if __name__=="__main__":
    from app import app 
    with app.app_context():
        db.create_all()