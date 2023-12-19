from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fly_app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# upload and store resume
def upload_resume(user_id, resume_file):
    with open(resume_file, 'rb') as f:
        resume_data = f.read()
    '''
    query db for user by user_id
    user.resume = resume_data
    commit()
    '''

# download and retrieve resume
def download_resume(user_id):
    # query db for user and return user.resume
    return

downloaded_resume = download_resume(...)
if downloaded_resume:
    # write downloaded_resume to new file
    with open("downloaded_resume.pdf", 'wb') as f:
        f.write(downloaded_resume)
