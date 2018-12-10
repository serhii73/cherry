import cherrypy
from cherrypy.test import helper

from tut12 import StringGenerator


class SimpleCPTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(StringGenerator(), "/", {})

    def test_index(self):
        self.getPage("/")
        self.assertStatus("200 OK")

    def test_generate(self):
        self.getPage("/generate")
        self.assertStatus("200 OK")

