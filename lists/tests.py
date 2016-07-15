from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from lists.views import index

# Create your tests here.

class IndexTest(TestCase):

    def test_root_url_resolves_to_index_view(self):

        found = resolve('/')

        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):

        request = HttpRequest()

        response = index(request)
        
        excepted_html = render_to_string("index.html")

        self.assertEqual(response.content.decode(), excepted_html)
