from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=10)
def job():
    subprocess.run(["python3", "bot.py"])
sched.start()
