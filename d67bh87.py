import time
import random
import requests
import prometheus_client as prom


req_summary = prom.Summary('python_my_req_example', 'Time spent processing a request')


@req_summary.time()


def process_request(t):
   time.sleep(t)


if __name__ == '__main__':

   counter = prom.Counter('python_my_counter', 'This is my counter')
   gauge = prom.Gauge('python_my_gauge', 'This is my gauge')
   histogram = prom.Histogram('python_my_histogram', 'This is my histogram')
   summary = prom.Summary('python_my_summary', 'This is my summary')
   prom.start_http_server(8000)

   while True:
       counter.inc(1)
       gauge.set(1)
       histogram.observe(1)
       summary.observe(1)
       process_request(1)

       time.sleep(1)
