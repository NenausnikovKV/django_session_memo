from django.test import Client, TestCase


class PageInterfaceTest(TestCase):
    client = Client()

    def test_request_count(self):
        response = self.client.get("/session/")
        self.assertContains(response, text="Session request count", status_code=200)

