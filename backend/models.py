from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base() # base class that all database tables inherit from

# User table - stores users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True )
    created_at = Column(DateTime, default = datetime.utcnow)

    # connects user to submissions and progress
    submissions = relationship("Submission", back_populates= "user")
    progress = relationship("Progress", back_populates = "user")

# Problem table - stores coding problems
class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    difficulty = Column(String)  # easy, medium, hard
    category = Column(String)  # arrays, graphs
    created_at = Column(DateTime, default=datetime.utcnow)
    
    submissions = relationship("Submission", back_populates="problem")

# Submissions table - stores user's code and pseudocode
class Submission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    pseudocode = Column(Text)   # user's thinking & approach
    code = Column(Text)         # user's actual code
    feedback = Column(Text)     # AI mentor questions/hints
    submitted_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="submissions")
    problem = relationship("Problem", back_populates="submissions")

# Progress table - tracks user growth over time
class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String)
    problems_attempted = Column(Integer, default=0)
    problems_solved = Column(Integer, default=0)
    common_mistakes = Column(Text)  # AI identified patterns
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="progress")