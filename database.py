#pip install sqlalchemy




from sqlalchemy import create_engine, Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///transcripts.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Transcript(Base):
    __tablename__ = "transcripts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    transcript = Column(Text)
    summary = Column(Text)

Base.metadata.create_all(engine)

def save_to_db(title, transcript, summary):
    session = Session()
    record = Transcript(title=title, transcript=transcript, summary=summary)
    session.add(record)
    session.commit()
    session.close()
