# main.py

from dotenv import load_dotenv
import os
import requests
import logging
from log_setup import setup_logging

# Load environment variables from the .env file
load_dotenv()

# Setup logging
setup_logging()

# Get the API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Create logger
logger = logging.getLogger(__name__)

# Check if the API key is loaded properly
if not groq_api_key:
    logger.error("GROQ_API_KEY is not set in the .env file")
else:
    logger.info("API Key Loaded Successfully")

# Example function to call Groq's API with the API key
def call_groq_math_function(operation, *args):
    """
    Function to call the Groq API to perform a math operation.
    """
    logger.info(f"Calling Groq API for operation: {operation} with arguments: {args}")
    
    url = "https://api.groq.com/math"  # Example URL for the math API
    headers = {"Authorization": f"Bearer {groq_api_key}"}

    # Example payload (adjust according to your actual API)
    data = {
        "operation": operation,
        "args": args
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        
        # Check if the API call was successful
        if response.status_code == 200:
            result = response.json()
            logger.info(f"API call successful. Result: {result}")
        else:
            logger.error(f"Failed to call API. Status code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred while calling the API: {e}")

# Example usage
if __name__ == "__main__":
    # Example: calling a math function 'add' with two numbers
    call_groq_math_function("add", 5, 3)
