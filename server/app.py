from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from config import BaseConfig
from db import initialize_db
from rest import initialize_api
import os
import glob

def remove_tmpfiles_job():
    files = glob.glob('/tmp/*')
    app.logger.info("executing cron job")
    app.logger.info(files)
    for f in [f for f in (files or [])]:
        app.logger.info("removing "+ f)
        os.remove(f)


sched = BackgroundScheduler(daemon=True)
sched.add_job(remove_tmpfiles_job,'interval',seconds=60)
sched.start()
app = Flask(__name__)
CORS(app)
app.config.from_object(BaseConfig)

initialize_db(app)

initialize_api(app)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')