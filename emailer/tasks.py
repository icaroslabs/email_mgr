from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from emailer.scripts import send_emails

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(day_of_week="*")))
def send_emails(campaign_id=1):
    logger.info("Start task")
    emailer = send_emails.Emailer()
    result = emailer.go(campaign_id)
    logger.info("Task finished: result = %i" % result)
