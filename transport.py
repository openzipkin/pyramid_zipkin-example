# -*- coding: utf-8 -*-
# main.py
import requests

def http_transport(ignored_stream_name, encoded_span):
    # The collector expects a thrift-encoded list of spans.
    requests.post(
        'http://localhost:9411/api/v2/spans',
        data=encoded_span,
        headers={'Content-Type': 'application/json'},
    )
