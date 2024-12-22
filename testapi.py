from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve and print the API key
api_key = os.getenv('SERPER_API_KEY')

if api_key is None:
    raise ValueError("SERPER_API_KEY is not set. Please check your .env file or environment variables.")
else:
    print("SERPER_API_KEY:", api_key)
