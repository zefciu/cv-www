from cvwww.tests import *

class TestAbilitiesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='abilities', action='index'))
        # Test response...
