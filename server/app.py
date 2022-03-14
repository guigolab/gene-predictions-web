from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from config import BaseConfig
from db import initialize_db
from rest import initialize_api
from db.models import TaxonFile,TaxonNode

#TODO
#implement log tracking and usage statistics (running time, average fasta size etc.)


# def remove_tmpfiles_job():
#     rs = GeneIdResults.objects()
#     for r in rs:
#         if r.jpg:
#             r.jpg.delete()
#         if r.ps:
#             r.ps.delete()
#         app.logger.info("deleting...")
#         r.delete()
# def drop_and_remove():
#     files = TaxonFile.objects()
#     for f in files:
#         f.file.delete()
#         f.delete()
#     TaxonFile.drop_collection()
#     taxons = TaxonNode.objects().delete()
#     TaxonNode.drop_collection() 


# sched = BackgroundScheduler(daemon=True) ## keep the scheduler for future uses
# sched.add_job(drop_and_remove,'interval',seconds=30)
# sched.start()
app = Flask(__name__)
CORS(app)
app.config.from_object(BaseConfig)

initialize_db(app)

initialize_api(app)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')