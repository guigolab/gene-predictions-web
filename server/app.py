from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from config import BaseConfig
from db import initialize_db
from rest import initialize_api
# from db.models import GeneIdResults

# def remove_tmpfiles_job():
#     rs = GeneIdResults.objects()
#     for r in rs:
#         if r.jpg:
#             r.jpg.delete()
#         if r.ps:
#             r.ps.delete()
#         app.logger.info("deleting...")
#         r.delete()

# sched = BackgroundScheduler(daemon=True) ## keep the scheduler for future uses
# sched.add_job(remove_tmpfiles_job,'interval',seconds=60)
# sched.start()
app = Flask(__name__)
CORS(app)
app.config.from_object(BaseConfig)

initialize_db(app)

initialize_api(app)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')