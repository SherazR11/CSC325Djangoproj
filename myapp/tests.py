from django.test import TestCase
from django.urls import reverse


class PageViewTests(TestCase):
	def test_home_page(self):
		response = self.client.get(reverse("home"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
		self.assertContains(response, "<h1>Hello, welcome to my Django app!</h1>", html=True)

	def test_about_page(self):
		response = self.client.get(reverse("about"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
		self.assertContains(
			response,
			"<h1>About Page</h1><p>This is the about page of my Django app.</p>",
			html=True,
		)