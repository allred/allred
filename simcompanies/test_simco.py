#!/usr/bin/env pytest
from simco_base import *

def setup_function():
    pass

def teardown_function():
    rc = redis_client()
    for i in [
        "deleteme_list",
    ]:
        rc.delete(i)

def test_get_kinds_from_stores(capsys):
    d = get_kinds_from_stores()
    assert isinstance(d, dict)
    #with capsys.disabled():
    #    print({"debug": d})

def test_parse_retail_modeling(capsys):
    retail_modeling = "(Math.pow(price*2.995075 + (-7.061656 + (saturation - 0.5)/0.455885), 2.000000)*0.748513 + 20.189612)*amount"
    r = parse_retail_modeling(retail_modeling)
    with capsys.disabled():
        print({"debug": type(r)})

def test_redis_client(capsys):
    r = redis_client()
    assert isinstance(r, redis.client.Redis) 
    #with capsys.disabled():
    #    print({"debug": type(r)})

def test_redis_list_push_fifo(capsys):
    list_max = 5
    n = redis_list_push_fifo("deleteme_list", str(datetime.now()), list_max)
    assert n <= list_max + 1
    #with capsys.disabled():
    #    print({"debug": n})
