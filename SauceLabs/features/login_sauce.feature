@allure.label.owner:EderMorales
Feature: Login en el sistema Swag Labs
    Como usuario de Swag Labs
    Quiero poder iniciar sesión en la plataforma
    Para acceder al inventario de productos disponibles

    Background:
        Given que el usuario esta en la pagina Login

    @login_valido
    Scenario: Inicio de sesion exitoso con credenciales validas
        When ingresa el nombre de usuario "standard_user"
        And ingresa el password "secret_sauce"
        And hace clic en el boton de Login
        Then deberia ser redirigido a la pagina "Products"

# @login_invalido
# Scenario: Inicio de sesión fallido con credenciales inválidas
#     #Given que el usuario esta en la pagina Login
#     When ingresa el nombre de usuario "standard_user"
#     And ingresa una contraseña incorrecta "clave_incorrecta"
#     And hace clic en el boton de Login
#     Then debería ver un mensaje de error "Epic sadface: Username and password do not match any user in this service"

# @login_campos_vacios
# Scenario: Inicio de sesión con campos vacíos
#     #Given que el usuario esta en la pagina Login
#     When deja el campo de usuario vacío
#     And deja el campo de contraseña vacío
#     And hace clic en el boton de Login
#     Then debería ver un mensaje de error de datos incompletos "Epic sadface: Username is required"

# @login_usuario_bloqueado
# Scenario: Intento de inicio de sesión con usuario bloqueado
#     #Given que el usuario esta en la pagina Login
#     When ingresa el nombre de usuario bloqueado "locked_out_user"
#     And ingresa el password "secret_sauce"
#     And hace clic en el boton de Login
#     Then debería ver un mensaje de error de usuario bloqueado "Epic sadface: Sorry, this user has been locked out."