"""_summary_
Contiene todas las funciones para interactuar
click a elemento
llenar campo, etc
    """
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect, Page, Locator
import re


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.menu = page.get_by_text('Open Menu')
        self.a_logout = page.locator("//a[@id='logout_sidebar_link']")

    async def check_url(self, text):
        await expect(self.page, "..::No se encontró el url::.."
                     ).to_have_url(re.compile(f".*{text}"))

    async def check_title(self, text):
        await expect(self.page, f"..::No se encontró {text} en el título::..").to_have_title(text)

    async def check_text(self, locator, text):
        if text != None and locator != None:

            # Si locator es un Locator, usa su propio método
            if isinstance(locator, Locator):
                await expect(locator, f"No sé encontro el texto <{text}>").to_have_text(text)
            # Si locator es un string, usa page
            elif isinstance(locator, str):
                await expect(self.page, f"No sé encontro el texto <{text}>").to_have_text(text)
            else:
                raise ValueError(
                    "El locator debe ser un string o un objeto Locator")

    async def fill_to_textbox(self, locator, text):
        # Si locator es un Locator, usa su propio método fill
        if isinstance(locator, Locator):
            await locator.fill(text)
        # Si locator es un string, usa page.fill
        elif isinstance(locator, str):
            await self.page.fill(locator, text)
        else:
            raise ValueError(
                "El locator debe ser un string o un objeto Locator")

    async def click_to_elememt(self, locator):
        await expect(locator, "..::Elemento no localizado::..").to_be_visible()
        await locator.click()

    async def logout(self):
        await self.click_to_elememt(self.menu)
        await self.click_to_elememt(self.a_logout)
