#!/usr/bin/env pytest
from simco_base import *

def setup_function():
    pass

def test_redis_list_push_fifo(capsys):
    list_max = 5
    n = redis_list_push_fifo("deleteme_list", str(datetime.now()), list_max)
    assert n <= list_max + 1
    #with capsys.disabled():
    #    print({"debug": n})
