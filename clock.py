from apscheduler.schedulers.blocking import BlockingScheduler
import moodle_notify

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=8)
def timed_job():
    moodle_notify.moodle_notify()


sched.start()
