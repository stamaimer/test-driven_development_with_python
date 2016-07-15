from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import index

# Create your tests here.

class IndexTest(TestCase):

    def test_root_url_resolves_to_index_view(self):

        found = resolve('/')

        self.assertEqual(found.func, index)
