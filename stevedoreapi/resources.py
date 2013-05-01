import falcon
import logging


class GenericResource(object):
    """ All the standard resource things that every task should have

        * logging
        * database connection (TODO)
    """
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

    def on_get(self, req, resp, task_id=None):
        """Handles GET requests"""
        self.logger.debug("get: task")
        resp.status = falcon.HTTP_200

        self.logger.debug("Task ID: {0}".format(task_id))
        resp.body = 'Task Id: {0}!'.format(task_id)

    def on_post(self, req, resp, task_id=None):
        # todo read post data
        pass


class ResultResource(GenericResource):

    def __init__(self):
        super(ResultResource, self).__init__()

    def on_get(self, req, resp, result_id=None):
        """Handles GET requests"""
        self.logger.debug("get: result")
        resp.status = falcon.HTTP_200
        resp.body = 'Results!'


class ResultDetailResource(GenericResource):

    def __init__(self):
        super(ResultDetailResource, self).__init__()

    def on_get(self, req, resp, result_id, detail_id=None):
        """Handles GET requests"""
        self.logger.debug("get: result detail")
        resp.status = falcon.HTTP_200
        resp.body = 'Result Details!'
