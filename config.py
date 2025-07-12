import os
from dotenv import load_dotenv

# Load environment variables from .env file (recommended)
load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

if not RIOT_API_KEY:
    raise EnvironmentError("❌ RIOT_API_KEY not set. Create a .env file or set the environment variable.")
