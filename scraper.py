from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import time

def fetch_html(url):
    """Usa Selenium con Microsoft Edge para obtener el HTML renderizado."""
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  # Opcional: comentar para ver el navegador
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Inicializar el navegador Edge con WebDriverManager
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(5)  # Espera para que cargue el contenido dinámico

    html = driver.page_source
    driver.quit()
    return html

def parse_products(html):
    """Extrae los productos del HTML renderizado usando BeautifulSoup."""
    soup = BeautifulSoup(html, "html.parser")
    productos = []

    for prod in soup.select("div.product-card-default"):
        nombre_elem = prod.select_one("p.CardName__CardNameStyles-sc-147zxke-0")
        precio_elem = prod.select_one("p.CardBasePrice__CardBasePriceStyles-sc-1dlx87w-0")
        imagen_elem = prod.select_one("figure img")

        nombre = nombre_elem.get_text(strip=True) if nombre_elem else "N/A"
        precio = precio_elem.get_text(strip=True) if precio_elem else "N/A"
        imagen = imagen_elem["src"] if imagen_elem and imagen_elem.has_attr("src") else "N/A"

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "imagen": imagen,
            })

    return productos
