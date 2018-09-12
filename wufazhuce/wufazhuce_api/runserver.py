from service import app


if __name__ == '__main__':
    app.run(debug=True, port=5008)


# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from service import app


# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5008, address="127.0.0.1")
# IOLoop.instance().start()
