import logging

from models import S3Record

# Configure logging
logger = logging.getLogger("aws-lambda")
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Received event: %s" % event)
    # Example for S3 Event received.
    s3_record = S3Record(event)
    logger.info(
        "Received event: %s on bucket: %s for object: %s",
        s3_record.event_name,
        s3_record.bucket_name,
        s3_record.object_key,
    )
    # Some logic here for the received event.
    return event
