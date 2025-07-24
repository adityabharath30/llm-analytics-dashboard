from database.db_config import Base, engine
from database.models import PromptLog

Base.metadata.create_all(bind = engine)
