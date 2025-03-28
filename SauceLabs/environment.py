from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright
from models.base_page import BasePage

# Decorador para preparar el navegador


@fixture
async def browser_chrome(context):
    page = await async_playwright().start()
    browser = await page.chromium.launch(
        headless=False,
        slow_mo=700,
        channel="chrome"  # Cambia el navegador
    )
    # ingnora errores de https new_page(ignore_https_errors=True)
    context.page = await browser.new_page()
    return context.page

# Con fixture indica que antes de cada escenario tiene que crear el navegador


@async_run_until_complete
async def before_scenario(context, scenario):
    await use_fixture(browser_chrome, context)

    # Carga la clase para enviarle un entorno
    # base_page = BasePage(context.page)
    # base_page.load_env()


@async_run_until_complete
async def after_scenario(context, scenario):
    try:
        # Cierra sesion después de cada escenario
        cierra_sesion = BasePage(context.page)
        await cierra_sesion.logout()

    except AssertionError as e:
        # PAra los casos que no iniciarion sesión
        print("***No se puede cerrar sesión, ya que no se ha iniciado sesión")
    finally:
        # Cierra el navegador después, aún si fallo el logout
        await context.page.close()
