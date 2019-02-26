# -*- coding: utf-8 -*-
# backend.py
import datetime

from py_zipkin import Encoding
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from transport import http_transport
from wsgiref.simple_server import make_server

@view_config(route_name='print_date')
def print_date(request):
    return Response(str(datetime.datetime.now()))

def main():
    settings = {}
    settings['service_name'] = 'backend'
    settings['zipkin.encoding'] = Encoding.V2_JSON
    settings['zipkin.transport_handler'] = http_transport

    config = Configurator(settings=settings)
    config.include('pyramid_zipkin')
    config.add_route('print_date', '/api')
    config.scan()

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 9000, app)
    print('Backend listening on http://localhost:9000/api')
    server.serve_forever()

if __name__ == '__main__':
    main()
