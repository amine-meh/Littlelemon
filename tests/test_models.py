from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(title="Waffles", price=2, inventory=20)
    self.assertEqual(item, "Waffles : 2")