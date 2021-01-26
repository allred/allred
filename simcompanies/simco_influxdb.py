#!/usr/bin/env python
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token_influxdb = os.environ["SIMCO_INFLUXDB_TOKEN"]
url_influxdb = "https://us-east-1-1.aws.cloud2.influxdata.com"
org_influxdb = "mikejallred@gmail.com"
bucket_influxdb = "mikejallred's Bucket"

def influxdb_client():
    client = InfluxDBClient(url=url_influxdb, token=token_influxdb)
    return client

"""
point = Point("mem")\\
  .tag("host", "host1")\\
  .field("used_percent", 23.43234543)\\
  .time(datetime.utcnow(), WritePrecision.NS)

write_api.write(bucket, org, point)
"""
"""
query = f'from(bucket: \\"{bucket}\\") |> range(start: -1h)'
tables = client.query_api().query(query, org=org)
"""
