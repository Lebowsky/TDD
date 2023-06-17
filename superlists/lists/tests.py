from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    """ home page test """

    def test_uses_home_template(self):
        """ test: uses home template """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
