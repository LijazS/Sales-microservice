import logging
import os

def setup_logging():

    service_name = os.getenv("SERVICE_NAME", "auth-service")

    logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s | %(levelname)s | {service_name} | %(name)s | %(message)s",
    )