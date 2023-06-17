from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    """ smoke test """

    def test_bad_maths(self):
        """ test bad maths """

        self.assertEqual(1 + 1, 3)
