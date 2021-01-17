from celery import Celery
import simco_celery_config

app = Celery("simco_celery")
app.config_from_object("simco_celery_config")

@app.task
def printer(x):
    print(x)
