# test page -> saucedemo.com
from playwright.sync_api import Page
import pytest
# Ejecutar un test basado en el browser
# skipear el resto de browsers
# @pytest.mark.only_browser("chromium") # -> el test_title ejecutar solamente en chromium
def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    # usar una asertion para validar el nombre del titulo
    assert page.title() == "Swag Labs"
    # para ver la pagina tenemos que usar en consola, el comando pytest --headed
# @pytest.mark.skip_browser("chromium") # -> skipea un brwoser
def test_inventory_page(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    # validar el texto del h3
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    page.pause()