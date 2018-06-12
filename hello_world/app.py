from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    print('Incoming request')
    return "hey"
    return Response('<body><h1>Hello World!</h1></body>')
def hello_techa(request):
    print('Incoming request')
    return Response('<body><h1>Hi techa</h1></body>')


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello')
        config.add_view(hello_world, route_name='hello')
        config.add_route('helloTecha', '/hello/techa')
        config.add_view(hello_techa, route_name='helloTecha')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
