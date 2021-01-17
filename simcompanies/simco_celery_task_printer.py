#!/usr/bin/env python
import os
from simco_celery import printer

msg = os.popen("date").read()
printer.delay(f"yo it's {msg}")
