def test_example_is_working(page):
    page.goto("https://maskarad-grim.ru/product/akvagrim-superstar-5-gr-zelenyy")
    assert page.inner_text('h1') == 'Аквагрим Superstar 5 гр зеленый'
    page.click("text=В корзину")
