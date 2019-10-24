from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
# API_KEY = os.getenv('API_KEY')
# API_URL = os.getenv('API_URL')
# CLAN = os.getenv('CLAN')