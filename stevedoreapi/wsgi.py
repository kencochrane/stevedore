import falcon

# falcon.API instances are callable WSGI apps
from resources import TaskResource, ResultResource, ResultDetailResource


wsgi_app = api = falcon.API()

# Resources are represented by long-lived class instances
task = TaskResource()
result = ResultResource()
result_detail = ResultDetailResource()

# things will handle all requests to the '/things' URL path
api.add_route('/task/', task)
api.add_route('/task/{task_id}/', task)
api.add_route('/result/', result)
api.add_route('/result/{result_id}/', result)
api.add_route('/result/{result_id}/detail/', result_detail)
api.add_route('/result/{result_id}/detail/{detail_id}/', result_detail)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, wsgi_app)
    print "Starting server http://localhost:8080"
    srv.serve_forever()
