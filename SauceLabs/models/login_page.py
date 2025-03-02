"""_summary_
Acciones propias de login page
    """

from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright, expect, Page
from models.base_page import BasePage
import time


class LoginPage(BasePage,):
    def __init__(self, page: Page):
        self.page = page
        self.user_textbox = page.locator('//input[@name="user-name"]')
        self.password_textbox = page.locator('//input[@name="password"]')
        self.btn_login = page.locator('//input[@id="login-button"]')
        self.products_header = page.locator('//div[@class="product_label"]')

    async def check_url(self, text):
        return await super().check_url(text)

    async def check_title(self, text):
        return await super().check_title(text)

    async def fill_user(self, text):
        await self.fill_to_textbox(self.user_textbox, text)

    async def fill_password(self, text):
        await self.fill_to_textbox(self.password_textbox, text)

    async def click_btn_login(self):
        await self.click_to_elememt(self.btn_login)

    async def check_text(self, text):
        return await super().check_text(self.products_header, text)
