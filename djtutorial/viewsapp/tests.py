from django.test import TestCase
from model_bakery import baker
from .models import Products, Category
from django.urls import reverse
# Create your tests here.

class ProductModelTest(TestCase):
    
    def test_product_created(self):
        # product = Products.objects.create(
        #     product_name = 'ABC Mobile',
        #     product_description = "An electronic device use to communicate.",
        #     product_quantity = 200,
        #     product_category = 'Electronics'
        # )
        
        product = baker.make(Products)
        product2 = baker.make(
            Products,
            product_name = 'Ear buds',
            product_quantity = 300,
        )
        
        
        self.assertIsNotNone(product.id)
        self.assertIsNotNone(product2.id)
        
    def test_product_created_count(self):
        product = baker.make(Products, _quantity=5)
        
        self.assertEqual(Products.objects.count(), 5)
        
    def test_product_created_foreign_key(self):
        category = baker.make(Category, product_category="Fruits")
        
        product = baker.make(Products, category = category, product_name="Mango")
        
class ProductDetailViewTest(TestCase):
    def test_product_detail_page(self):
        product = baker.make(Products, product_name = "Laptop")
        
        # url = reverse('product_details', kwargs={"id": product.id})
        url = reverse('product_view_cls', kwargs={'pk':product.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")
        