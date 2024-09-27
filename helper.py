from dotenv import load_dotenv
import os

load_dotenv()

def get_env_variable(variable_name):
    """
    Get the value of an environment variable.

    Args:
        variable_name (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable.
    """
    return os.getenv(variable_name)
