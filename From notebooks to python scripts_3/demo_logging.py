import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),            # terminal
        logging.FileHandler("app.log")      # file
    ]
)

logging.info("Program started")
logging.debug("Debugging code")
logging.warning("This is a warning message")
logging.error("This is an error message")