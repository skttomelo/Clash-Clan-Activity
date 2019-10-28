from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / 'config.env'
load_dotenv(dotenv_path=env_path)
CR_API_KEY = os.getenv('CR_API_KEY')
CR_API_URL = os.getenv('CR_API_URL')
RA_API_KEY = os.getenv('RA_API_KEY')
RA_API_URL = os.getenv('RA_API_URL')
CLAN = os.getenv('CLAN')