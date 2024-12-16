# log_setup.py
import logging

def setup_logging(log_file="app.log"):
    """
    Setup logging configuration.
    """
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,  # You can change this to DEBUG for more verbose logging
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    logger.info("Logging setup complete.")

