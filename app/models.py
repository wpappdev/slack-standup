from datetime import datetime

from sqlalchemy import Column, Integer, String

from . import db


class Submission(db.Model):
    __tablename__ = 'submission'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(20), unique=False)
    username = Column(String(50), unique=False)
    standup_submission = Column(String(), unique=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)