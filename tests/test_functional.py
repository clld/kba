import pytest


@pytest.mark.parametrize(
    "method,path",
    [
        ('get_html', '/'),
        ('get_html', '/languages'),
        ('get_html', '/parameters'),
        ('get_html', '/languages/blenaq-h'),
        ('get_html', '/parameters/eye_l5'),
    ])
def test_pages(app, method, path):
    getattr(app, method)(path)
