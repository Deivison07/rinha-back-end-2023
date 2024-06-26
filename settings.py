import os
from dotenv import load_dotenv
load_dotenv()

database_host = os.getenv("DATABASE_IP")
database_pass = os.getenv("DATABASE_PASS")
database_port = os.getenv("DATABASE_PORT")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
DATABASE_CONNECTION_URL = f"postgresql://{database_user}:{database_pass}@{database_host}:{database_port}/{database_name}"