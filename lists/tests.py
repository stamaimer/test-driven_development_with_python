from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from lists.views import index
from lists.models import Item

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

    def test_index_can_save_a_POST_request(self):

        request = HttpRequest()

        request.method = "POST"

        request.POST["item_text"] = "A new list item"

        response = index(request)

        self.assertIn("A new list item", response.content.decode())

        excepted_html = render_to_string(
            "index.html",
            {"new_item_text": "A new list item"}
        )

        self.assertEqual(response.content.decode(), excepted_html)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_item(self):

        first_item = Item()

        first_item.text = "The first (ever) list item"

        first_item.save()

        second_item = Item()

        second_item.text = "Item the second"

        second_item.save()

        saved_items = Item.objects.all()

        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]

        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first (ever) list item")

        self.assertEqual(second_saved_item.text, "Item the second")
