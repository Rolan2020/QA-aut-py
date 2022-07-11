from playwright.sync_api import sync_playwright


# URL
URL = 'https://www.phptravels.net/login'
DASHBOARD_URL = 'https://www.phptravels.net/account/dashboard'

# Login Xpaths
EMAIL_TEXTBOX = "//input[@placeholder='Email']"
EMAIL = "user@phptravels.com"
PASSWORD_TEXTBOX = "//input[@placeholder='Password']"
PASSWORD = "demouser"
SUBMIT_BUTTON = "//button[@type='submit']"
# //button[@class='btn btn-default btn-lg btn-block effect ladda-button waves-effect']

# Verify Xpaths
# class ' waves-effect' lleva una espacio adelante
MY_BOOKINGS_BUTTON = "//a[@class=' waves-effect' and @href='https://www.phptravels.net/account/bookings']"
MY_BOOKINGS_VERIFY = "//h3[text()='My Bookings']"
ADD_FUNDS_BUTTON = "//a[@class=' waves-effect' and @href='https://www.phptravels.net/account/add_funds']"
ADD_FUND_VERIFY = "//h3[text()='Add Funds']"
PROFILE_BUTTON = "//a[@class=' waves-effect' and @href='https://www.phptravels.net/account/profile']"
PROFILE_VERIFY = "//h3[text()='Profile Information' and @class='title']"
#"//h3[text()='Profile Information']"

LOGOUT_BUTTON = "//a[@class=' waves-effect' and @href='https://www.phptravels.net/account/logout']"


# with -> se usa para gestionar el contexto en python
# inicia y cierra el contexto cuando llamamos -> sync_playwright()

# creamos funcion para ejecutar pytest
# comando -> pytest --browser chromium --headed --slowmo 3000
def test_phptravel_flow(page):
    # open site
    page.goto(URL)
    # enter email
    page.fill(EMAIL_TEXTBOX, EMAIL)
    # enter pass
    page.fill(PASSWORD_TEXTBOX, PASSWORD)
    # click on button
    page.click(SUBMIT_BUTTON)
    # verifica cambio URL
    page.wait_for_url(DASHBOARD_URL)
    # click en booking button
    page.click(MY_BOOKINGS_BUTTON)
    # verifica q esta en la pagina de bookings
    page.wait_for_selector(MY_BOOKINGS_VERIFY)
    # click en Add Fund button
    page.click(ADD_FUNDS_BUTTON)
    # verifica que esta en la pagina de add funds
    page.wait_for_selector(ADD_FUND_VERIFY)
    # click en profile
    page.click(PROFILE_BUTTON)
    # verifica que esta en Profile
    page.wait_for_selector(PROFILE_VERIFY)
    # deslogear cuenta con logout button
    page.click(LOGOUT_BUTTON)

    # Cierre de pagina y browser
    page.close()
 # SHIFT + TAB = identar hacia atras


