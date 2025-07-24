from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from database.db_config import Base

class PromptLog(Base):
    __tablename__ = "prompt_logs"

    id = Column(Integer, primary_key = True, index = True)
    prompt = Column(Text, nullable = False)
    response = Column(Text)
    model = Column(String(50))
    tokens = Column(Integer)
    cost = Column(Float)
    latency_ms = Column(Integer)
    timestamp = Column(DateTime, default = datetime.utcnow)
    


