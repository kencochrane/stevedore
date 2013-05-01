import falcon
import logging


class GenericResource(object):

    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(self.LOGGING_FORMAT)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

class TaskResource(GenericResource):

    def __init__(self):
        super(TaskResource, self).__init__()

    def on_get(self, req, resp):
        """Handles GET requests"""
        self.logger.debug("get: task")
        resp.status = falcon.HTTP_200
        resp.body = 'Tasks!'


class ResultResource(GenericResource):

    def __init__(self):
        super(ResultResource, self).__init__()

    def on_get(self, req, resp):
        """Handles GET requests"""
        self.logger.debug("get: result")
        resp.status = falcon.HTTP_200
        resp.body = 'Results!'
