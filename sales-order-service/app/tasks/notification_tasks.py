from app.core.celery_app import celery


@celery.task(name="order.send_order_created_notification")
def send_order_created_notification(payload: dict):
    celery.send_task(
        "notification.send_email",
        args=[{
            "type": "ORDER_CREATED",
            "payload": payload
        }],
        queue="notification_queue"
    )


@celery.task(name="order.send_order_confirmed_notification")
def send_order_confirmed_notification(payload: dict):
    celery.send_task(
        "notification.send_email",
        args=[{
            "type": "ORDER_CONFIRMED",
            "payload": payload
        }],
        queue="notification_queue"
    )


@celery.task(name="order.send_order_cancelled_notification")
def send_order_cancelled_notification(payload: dict):
    celery.send_task(
        "notification.send_email",
        args=[{
            "type": "ORDER_CANCELLED",
            "payload": payload
        }],
        queue="notification_queue"
    )