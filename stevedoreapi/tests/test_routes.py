import falcon
import falcon.testing as testing

from ..resources import TaskResource, ResultResource, ResultDetailResource


# see test_http_method_routing for example
class TaskRouting(testing.TestBase):

    def before(self):
        self.resource_task = TaskResource()
        self.api.add_route('/task/', self.resource_task)
        self.api.add_route('/task/{task_id}/', self.resource_task)

    def test_get(self):
        self.simulate_request('/task/')
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertTrue(self.resource_task.called)

    def test_get_with_task_id(self):
        self.simulate_request('/task/1/')
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertTrue(self.resource_task.called)

    #TODO POSTs


class ResultRouting(testing.TestBase):

    def before(self):
        self.resource_result = ResultResource()
        self.api.add_route('/result/', self.resource_result)
        self.api.add_route('/result/{result_id}/', self.resource_result)

    def test_get(self):
        self.simulate_request('/result/')
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertTrue(self.resource_result.called)

    def test_get_with_task_id(self):
        self.simulate_request('/result/1/')
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertTrue(self.resource_result.called)

    # TODO POSTs


class ResultDetailRouting(testing.TestBase):

    def before(self):
        self.resource_detail = ResultDetailResource()
        self.api.add_route('/result/{result_id}/detail/', self.resource_detail)
        self.api.add_route('/result/{result_id}/detail/{detail_id}/', self.resource_detail)

    def test_get(self):
        self.simulate_request('/result/')
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertTrue(self.resource_detail.called)

    def test_get_with_task_id(self):
        self.simulate_request('/result/1/')
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertTrue(self.resource_detail.called)

        # TODO POSTs
