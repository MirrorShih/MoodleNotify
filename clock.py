from apscheduler.schedulers.blocking import BlockingScheduler
import moodle_notify
import os

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=(int(os.environ.get("NOTIFY_TIME"))+16) % 24)
def timed_job():
    moodle_notify.moodle_notify()


sched.start()
