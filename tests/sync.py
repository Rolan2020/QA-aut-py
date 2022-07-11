# instalar playwright test for VS code
# 1er test sincrono
from playwright.sync_api import sync_playwright
# la p va estar usando los comandos de la libreria sync
with sync_playwright() as p:
    # pasar a launch el parametro de headless = false
    browser = p.chromium.launch(headless=False) # variable con equivalencia al chromium
    
    page = browser.new_page() # declaramos una variable y le asignamos browser
    # usamos el metodo new_page() de browser
    # usamos page para usar .goto -> visitar una website
    page.goto("http://playwright.dev")
    # hacer un screenshot con la direccion y nombre
    page.screenshot(path="demo.png")
    browser.close() # cerramos el browser
