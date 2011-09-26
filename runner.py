if __name__ == '__main__': 
    from gevent.wsgi import WSGIServer
    from flog import app
    
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
