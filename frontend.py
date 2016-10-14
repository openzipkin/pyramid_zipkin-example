# -*- coding: utf-8 -*-
# frontend.py
import requests

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from py_zipkin.zipkin import create_http_headers_for_new_span
from transport import http_transport
from wsgiref.simple_server import make_server

@view_config(route_name='call_backend')
def call_backend(request):
    headers = {}
    headers.update(create_http_headers_for_new_span())
    backend_response = requests.get(
        url='http://localhost:9000/api',
        headers=headers,
    )
    return Response(backend_response.text)

def main():
    settings = {}
    settings['service_name'] = 'frontend'
    settings['zipkin.transport_handler'] = http_transport
    settings['zipkin.tracing_percent'] = 100.0

    config = Configurator(settings=settings)
    config.include('pyramid_zipkin')
    config.add_route('call_backend', '/')
    config.scan()

    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8081, app)
    print('Frontend listening on http://localhost:8081')
    server.serve_forever()

if __name__ == '__main__':
    main()
