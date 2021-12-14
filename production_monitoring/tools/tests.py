import pytest



@pytest.mark.django_db
def test_product_page(client, example_product):
    response = client.get(f'/product/{example_product.id}/')
    assert response.status_code == 200
    assert response.context['description'] == 'Example Test Description'
    assert response.context['name'] == 'product'
    assert response.context['price'] == 356


@pytest.mark.django_db
def test_product_addition(client):
    response = client.post('/product/add/',
                           {'name': 'a test product',
                            'description': 'a test description', 'price': 500})
    product = Product.objects.get(name='a test product')
    assert response.status_code == 302
    assert product.description == 'a test description'
    assert product.price == 500