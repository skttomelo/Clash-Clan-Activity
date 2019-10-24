from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
# API_KEY = os.getenv('API_KEY')
# API_URL = os.getenv('API_URL')
# CLAN = os.getenv('CLAN')
CLAN = "%23YYLQVU"
API_KEY = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc4MDE0YzQyLTQ2MTMtNGE3ZS1iMzk0LTJmYjc1MDUxZWU3ZSIsImlhdCI6MTU2NTc0NjgxNywic3ViIjoiZGV2ZWxvcGVyL2ZhM2YxYjA3LWI1Y2EtNzk4Ny1jNzMzLTBmMTI5ZDAwNTM2OCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNC4xNTkuMTE0LjIwMCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.mPSw8k0qZ8HsKFh71WqjI_10508MH1pSmtudqO3y_DHi6UF83GEMlZ2e9NFOGJASl3AssU_gqCz2DDFv-FWGzA"
API_URL = "https://api.clashroyale.com/v1/"