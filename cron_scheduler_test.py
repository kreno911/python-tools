from datetime import datetime, timedelta
# Try out the AP scheduler (move if needed)
# https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html#module-apscheduler.triggers.cron
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

print("Starting cron...")
def update():
    print("Updating: ", datetime.utcnow())

# Run every minute
sched.add_job(update, 'cron', minute='*/1')
sched.start()
