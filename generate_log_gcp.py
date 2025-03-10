import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging import structs
import logging

# Instantiates a client
client = google.cloud.logging.Client()

# Setup basic configuration for Python logging to log to Cloud Logging
client.setup_logging()

# Create logger instance
logger = logging.getLogger("my-log")

# Example log entries
logger.info("This is an info message logged to Google Cloud Logging.")

# If you want to create custom logs, you can do so by writing log entries directly.
def create_custom_log_entry():
    # Prepare the log entry with details like log name, severity, and payload
    log_name = "my_custom_log"
    logger = client.logger(log_name)
    log_entry = {
        "severity": "INFO",  # The severity level of the log entry
        "textPayload": "Srikant This is a custom log entry from the Python script.",
        "labels": {
            "custom_label": "example_value"
        }
    }
    # Write the log entry to Google Cloud Logging
    logger.log_struct(log_entry)

# Example custom log entry
create_custom_log_entry()

print("Log entries created successfully.")
