from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.orm import relationship, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base
from fly_app import Base, engine
from pydantic import BaseModel


Session = sessionmaker(bind=engine)
session = Session()

mapper_registry = registry()
mapper_registry.configure()

Base = declarative_base()


# USERS
class SignUp(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    profession = Column(String(255), nullable=False)

# JOB POSTINGS / AVAILABLE JOBS
class JobPostings(Base):
    __tablename__ = "job_postings"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    job_description = Column(String(500), nullable=False)
    location = Column(String(255), nullable=False)
    renumeration = Column(String(255), nullable=False)
    time_posted = Column(String(255), nullable=False)

# APPLICANTS
class JobApplicants(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    profession = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    cover_letter = Column(String(500), nullable=False)
    resume = Column(String(500), nullable=False)
    applicant_id = Column(Integer, nullable=False)
    job_application_status_id = Column(Integer, nullable=False)

# COMPANIES
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
    website = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    industry = Column(String(255), nullable=False)

# JOB CATEGORY
class JobCategory(Base):
    __tablename__ = "job_categories"

    id = Column(Integer, primary_key=True)
    job_category = Column(String(255), nullable=False)
    category_description = Column(Integer, nullable=True)

# JOB SKILL
class JobSkill(Base):
    __tablename__ = "job_skills"

    id = Column(Integer, primary_key=True)
    skills = Column(String(255), nullable=False)

# JOB APPLICATION STATUS
class JobApplicationStatus(Base):
    __tablename__ = "job_application_statuses"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(length=None), nullable=False)

# SAVED JOBS
class SavedJobs(Base):
    __tablename__ = "saved_jobs"

    applicant_id = Column(Integer, primary_key=True)
    job_posting_id = Column(Integer, primary_key=True)
