import schedule
import time

def schedule_job(config, job_func):
    schedule_time = config.get_schedule_time()
    schedule.every().day.at(schedule_time).do(job_func)

    while True:
        schedule.run_pending()
        print("Checking again in 60 seconds...")
        time.sleep(60)
