import pytest

def test_home_page_title(page):
    # Simple test, load homepage and check title
    page.goto("https://wonderproxy.com")
    assert page.title() == 'Localization testing with confidence - WonderProxy'

# crear listas con los valores a ingresar en "Server Status"
@pytest.mark.parametrize("test_input", ["lansing", "orlando", "perth", "knoxville"])
# creamos la funcion con los parametros test_input
def test_check_server_status(page, test_input):
    # Check server status for multiple servers
    page.goto("https://wonderproxy.com/servers/status")
    # Ingresa los test_input
    server_status = page.inner_text("//a[@href='/servers/" + test_input + "']/ancestor::li/span[5]")
    # assertion de server
    assert server_status == "up"

"""
Correr en pytest
"""