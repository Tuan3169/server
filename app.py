from library import create_app
from gevent.pywsgi import WSGIServer
# from .library.config import POST
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()