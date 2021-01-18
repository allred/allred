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

def test_retail_modeling_calculate(capsys):
    retail_modeling = "(Math.pow(price*2.995075 + (-7.061656 + (saturation - 0.5)/0.455885), 2.000000)*0.748513 + 20.189612)*amount"
    price = 3.930373600259584
    saturation = 0.8583561299159979
    gd = retail_modeling_parse(retail_modeling)
    r = retail_modeling_calculate(gd, price, saturation)
    assert isinstance(r, float)

def test_retail_modeling_parse(capsys):
    retail_modeling = "(Math.pow(price*2.995075 + (-7.061656 + (saturation - 0.5)/0.455885), 2.000000)*0.748513 + 20.189612)*amount"
    r = retail_modeling_parse(retail_modeling)
    assert len(r.values()) == 7

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
