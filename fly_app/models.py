from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, CheckConstraint, LargeBinary
from sqlalchemy.orm import relationship, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base
from fly_app import Base, engine


Session = sessionmaker(bind=engine)
session = Session()

mapper_registry = registry()
mapper_registry.configure()

Base = declarative_base()


# USERS TABLE
class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, unique=True)
    username = Column(String)
    firstname = Column(String(255), nullable=False)
    middlename = Column(String(255))
    lastname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    hashed_password = Column(String)
    skills = Column(String)
    experience = Column(String)
    education = Column(String)
    resume = Column(LargeBinary)
    applied_jobs = relationship("jobs", backref='applicants', secondary='job_applicants')
    saved_jobs = relationship("jobs", backref='saved_by', secondary='saved_jobs')


# CLIENTS/EMPLOYERS TABLE
class Companies(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, unique=True, primary_key=True)
    company_name = Column(String)
    contact_information = Column(String)
    posted_jobs = ForeignKey("jobs.job_id")


# JOBS TABLE
class Jobs(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, unique=True, primary_key=True)
    title = Column(String)
    company_id = ForeignKey("compamies.company_id")
    location = Column(String)
    job_type = Column(String, CheckConstraint("job_type IN ('full-time', 'part-time', 'contract')"))
    description = Column(String)
    requirements = Column(String)
    responsibilities = Column(String)
    benefits = Column(String)
    salary_range = Column(String)
    posted_date = Column(DateTime)
    deadline = Column(DateTime)
    applicants = relationship('users', backref='applied_jobs', secondary='job_applicants')
    saved_by = relationship('users', backref='saved_jobs', secondary='saved_jobs')


class JobApplicants(Base):
    __tablename__ = 'job_applicants'

    job_applicant_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    job_id = Column(Integer, ForeignKey("jobs.job_id"))


# SAVED JOBS
class SavedJobs(Base):
    __tablename__ = "saved_jobs"

    saved_job_id = Column(Integer, primary_key=True)
    applicant_id = Column(Integer, ForeignKey("users.user_id"))
    job_posting_id = Column(Integer, ForeignKey("jobs.job_id"))


# SKILLS TABLE
class Skills(Base):
    __tablename__ = "skills"

    skill_id = Column(Integer, unique=True, primary_key=True)
    skill_name = Column(String)
    related_jobs = Column(String, default="[]") # list of job_ids


# APPLICATIONS TABLE
class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, unique=True, primary_key=True)
    job_id = ForeignKey("jobs.job_id")
    applicant_id = ForeignKey("users.user_id")
    cover_letter = Column(String)
    submitted_date = Column(DateTime)
    application_status = Column(String, CheckConstraint("application_status IN ('pending', 'shortlisted', 'rejected', 'hired')" ))     # pending, shortlisted, rejected, hired)


# SEARCH TABLE
# class Search(Base):
#     __tablename__ = "searches"

#     search_id = Column(Integer, unique=True, primary_key=True)
#     keywords = Column(String)
#     location = Column(String)
#     job_type = Column(String)
#     skill_ids = Column(String)
#     salary_range = Column(String)


class JobCategories(Base):
    __tablename__ = "job_categories"

    category_id = Column(Integer, unique=True, primary_key=True)
    category_name = Column(String)
    related_jobs = Column(String, default="[]")


class Reviews(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, unique=True, primary_key=True)
    company_id = ForeignKey("companies.company_id")
    applicant_id = ForeignKey("users.user_id")
    rating = Column(Integer)
    review = Column(String)
    date = Column(DateTime)


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, unique=True, primary_key=True)
    sender_id = ForeignKey("users.user_id")
    receiver_id = ForeignKey("companies.company_id")
    message = Column(String)
    date = Column(DateTime)


class Notifications(Base):
    __tablename__ = "notifications"

    notification_id = Column(Integer, unique=True, primary_key=True)
    sender_id = ForeignKey("companies.company_id")
    receiver_id = ForeignKey("users.user_id")
    message = Column(String)
    date = Column(DateTime)
