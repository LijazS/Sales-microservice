from app.core.celery_app import celery

@celery.task(name="notification.send_signup_email")
def send_signup_email(payload):
    # This will NOT run here
    # It will be consumed by notification service worker
    pass