from behave import given, when, then
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright, expect
from models.login_page import LoginPage


@given("que el usuario esta en la pagina Login")
@async_run_until_complete
async def step_usuario_en_login(context):
    await context.page.goto("https://www.saucedemo.com/v1/index.html")

    # await context.page.pause()

    login = LoginPage(context.page)

    await login.check_url("saucedemo.com/v1/index.html")
    await login.check_title("Swag Labs")


@when('ingresa el nombre de usuario "{user}"')
@async_run_until_complete
async def step_ingresa_nombre_usuario(context, user):
    usuario = LoginPage(context.page)
    await usuario.fill_user(user)


@when('deja el campo de usuario vacío')
@async_run_until_complete
async def step_ingresa_nombre_usuario_vacio(context):
    usuario = LoginPage(context.page)
    await usuario.fill_user("")


@when('ingresa el password "{password}"')
@async_run_until_complete
async def step_ingresa_password(context,  password):
    user_password = LoginPage(context.page)
    await user_password.fill_password(password)


@when('ingresa una contraseña incorrecta "{password}"')
@async_run_until_complete
async def step_ingresa_password_incorrecta(context,  password):
    user_password = LoginPage(context.page)
    await user_password.fill_password(password)


@when('deja el campo de contraseña vacío')
@async_run_until_complete
async def step_ingresa_password_vacio(context):
    user_password = LoginPage(context.page)
    await user_password.fill_password("")


@when('hace clic en el boton de Login')
@async_run_until_complete
async def step_click_boton_loging(context):
    btn_login = LoginPage(context.page)
    await btn_login.click_btn_login()


@then('deberia ser redirigido a la pagina "{text}"')
@async_run_until_complete
async def step_usuario_redigido_pagina_principal(context, text):
    redirected = LoginPage(context.page)
    await redirected.check_text(text)


@then('debería ver un mensaje de error "{text}"')
@async_run_until_complete
async def step_error_user_password_no_match(context, text):
    error_msg = LoginPage(context.page)
    await error_msg.check_error_text(text)


@then('debería ver un mensaje de error de datos incompletos "{text}"')
@async_run_until_complete
async def step_error_datos_imcompletos(context, text):
    error_msg = LoginPage(context.page)
    await error_msg.check_error_text(text)


@then('debería ver un mensaje de error de usuario bloqueado "{text}"')
@async_run_until_complete
async def step_error_locked_user(context, text):
    error_msg = LoginPage(context.page)
    await error_msg.check_error_text(text)
