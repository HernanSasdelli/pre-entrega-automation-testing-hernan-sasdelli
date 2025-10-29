#####################################  Propósito #############################################
Pre-entrega del proyecto (hasta Clase 8): automatizar flujos básicos de **SauceDemo** con **Python + Pytest + Selenium**, validando login, inventario y carrito.

#####################################  Tecnologías #############################################
- Python 3.12
- Pytest
- Selenium WebDriver
- pytest-html (reporte)

#####################################  Requisitos previos ######################################
- Google Chrome instalado
- .venv


##################################### Instalación #############################################
-bash
##crear/activar venv (Windows)
python -m venv .venv
..venv\Scripts\activate


##################################### instalar dependencias ###############################
python -m pip install --upgrade pip
pip install -r requirements.txt


##################################### ejecucion de pruebas ###############################
-suite completa con reporte HTML
pytest -v --html=reports/reporte.html

##################################### Reporte y evidencias ###############################
El reporte se genera en reports/reporte.html
Si un test falla, se guarda captura automática en reports/ (lo maneja conftest.py)

##################################### CASOS DE PRUEBA #############################################
CP-01

id: CP-01
nombre: Automatización de Login
objetivo: Navegar a saucedemo.com, ingresar credenciales válidas y validar login exitoso.
precondiciones: Acceso a https://www.saucedemo.com/

datos de prueba: usuario=standard_user, contraseña=secret_sauce
pasos:

1-Abrir la URL de login

2-Ingresar usuario y contraseña

3+Clic en “Login”

resultado esperado: URL contiene /inventory.html y se visualiza “Products” o “Swag Labs”
estado: Aprovado
observaciones: URL /inventory.html y título Products visibles
severidad: 2
prioridad: 1

CP-02

id: CP-02
nombre: Navegación y Verificación del Catálogo
objetivo: Validar título del inventario, existencia de productos y elementos clave de UI.
precondiciones: CP-01 aprobado (usuario logueado)
datos de prueba: N/A
pasos:

1-Leer el título de la página de inventario

2-Contar productos visibles

3Registrar nombre y precio del primer producto

4-Verificar presencia de menú y filtros

resultado esperado: Título “Products”; al menos 1 producto visible; se obtiene nombre y precio del primero; menú y filtros presentes
estado: Aprobado
observaciones: título OK; productos visibles; primero = Sauce Labs Backpack – $29.99; menú y filtro “Name (A to Z)” presentes
severidad: 2
prioridad: 2


CP-03
id: CP-03
nombre: Interacción con Productos (Carrito)
objetivo: Agregar un producto y verificar contador del carrito y contenido.
precondiciones: CP-01 aprobado (en inventario)
datos de prueba: N/A
pasos:

1-Clic en “Add to cart” del primer producto

2-Verificar el badge (contador) del carrito

3-Abrir el carrito

4-Verificar que el producto agregado figure listado

resultado esperado: Badge = 1 tras agregar; el producto aparece en el carrito con su nombre
estado: Aprobado
observaciones: Item en el carrito, indica 1 y se puede ver al ingresar al carrito.
severidad: 2
prioridad: 2


SELECTORES A USAR
usuario: #user-name (XPath: //input[@id='user-name'])

password: #password (XPath: //input[@id='password'])

botón login: #login-button (XPath: //*[@id='login-button' or @data-test='login-button'])

título inventario: .title (XPath: //span[normalize-space()='Products'])

primer Add to cart: [id^="add-to-cart-"] (XPath: //button[contains(@id,'add-to-cart-')])

badge carrito: .shopping_cart_badge (XPath: //span[@class='shopping_cart_badge'])

icono carrito: .shopping_cart_link (XPath: //a[contains(@class,'shopping_cart_link')])

nombre 1er producto: .inventory_item_name (XPath: (//div[contains(@class,'inventory_item_name')])[1])

precio 1er producto: .inventory_item_price (XPath: (//div[contains(@class,'inventory_item_price')])[1])