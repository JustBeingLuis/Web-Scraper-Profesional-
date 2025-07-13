
# 🕷️ Web Scraper Profesional 

Este proyecto es una herramienta de **scraping profesional automatizado**, diseñada para extraer información de productos desde sitios web de comercio electrónico que utilizan contenido dinámico (renderizado con JavaScript). La aplicación genera automáticamente **informes en tres formatos**: `PDF`, `Excel` y `JSON`, incluyendo el **nombre del producto, precio e imagen** de cada ítem disponible.

> 🔎 Este scraper ha sido probado exitosamente con el sitio oficial de [Tiendas D1](https://domicilios.tiendasd1.com/), específicamente en la categoría de congelados.

---

## 📌 Características Principales

| Funcionalidad                        | Descripción |
|-------------------------------------|-------------|
| 🧠 Scraping inteligente              | Usa `Selenium` para procesar contenido dinámico. |
| 📦 Extracción de datos estructurados| Nombre, precio e imagen del producto. |
| 🧾 Exportación en formatos múltiples | JSON, Excel (`.xlsx`) y PDF con imágenes integradas. |
| 🛠️ Código modular y extensible       | Separación clara de funciones por archivo. |
| 💡 Adaptable a múltiples páginas    | Soporte para ajustar selectores y estructuras HTML. |

---

## 🚀 ¿Cómo funciona?

1. El usuario ingresa la URL de la página que desea scrapear.
2. Se lanza un navegador automatizado (como Edge o Brave) mediante Selenium.
3. Se espera a que cargue el contenido dinámico (productos).
4. Se extrae la información relevante utilizando `BeautifulSoup`.
5. Se generan 3 tipos de informes automáticamente:
   - 📄 `informe.pdf` con texto e imágenes.
   - 📊 `informe.xlsx` listo para análisis en Excel o Power BI.
   - 🧾 `informe.json` con la estructura de los datos.

---

## 📁 Estructura del proyecto

```
web-scraper-app/
├── main.py              # Script principal (ejecuta todo)
├── scraper.py           # Lógica de scraping y parsing HTML
├── reports.py           # Generación de informes PDF, Excel y JSON
├── requirements.txt     # Dependencias del proyecto
├── informe.xlsx         # Informe generado en Excel
├── informe.pdf          # Informe PDF con imágenes
├── informe.json         # Datos en formato estructurado
```

---

## 🔧 ¿Cómo adaptarlo a otras páginas?

Este scraper **es totalmente adaptable a otros sitios web**, pero es necesario comprender cómo funciona la estructura del HTML en cada caso. Aquí están los pasos para adaptarlo:

### 1. 🔍 Analiza el HTML de la nueva página

- Abre el navegador, haz clic derecho sobre el producto y selecciona **"Inspeccionar"**.
- Identifica el **contenedor principal** de cada producto (ej. `div.product-card`, `li.item`, etc.).
- Dentro de ese contenedor, ubica:
  - **Nombre del producto**: ¿está en un `<p>`, `<h2>`, `<span>`?
  - **Precio**: ¿es un `<p>`, `<div>`?
  - **Imagen**: busca la etiqueta `<img>` y asegúrate de extraer el atributo `src`.

### 2. ✍️ Ajusta los selectores CSS

Los selectores actuales funcionan solo para Tiendas D1. Para otros sitios debes modificar:

- La clase del **contenedor del producto**
- La clase y tipo de etiqueta donde se encuentra el **nombre**
- La clase y tipo de etiqueta donde está el **precio**
- La ubicación de la **imagen** (`img`) si existe

> ⚠️ **Importante:** El selector debe incluir tanto la **etiqueta HTML** como su clase, por ejemplo:  
> `p.nombre-producto`, `div.precio`, `img.product-image`.

### 3. ✅ Verifica que los datos estén bien extraídos

Puedes imprimir temporalmente los productos extraídos en consola con:

```python
print(productos)
```

y revisar si están correctos antes de generar los informes.

---

## 🧪 Requisitos del entorno

- Python 3.8 o superior
- Navegador **Microsoft Edge** (recomendado por compatibilidad con Selenium)
- Google Chrome o Brave (también soportados, con ajustes)
- Paquetes requeridos:
  - `selenium`
  - `bs4`
  - `requests`
  - `fpdf`
  - `pandas`
  - `openpyxl`
  - `webdriver-manager`
  - `Pillow`

---

## ⚙️ Uso del proyecto

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/web-scraper-app.git
cd web-scraper-app

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el scraper
python main.py
```

## 👨‍💻 Autor

**Luis Toscano**  
Estudiante de Ingeniería de Sistemas – UIS  
🔬 Proyecto desarrollado con fines investigativos y de portafolio.  
Presentado en el marco de prácticas de scraping profesional.

---

## 📄 Licencia

Este proyecto es de libre uso educativo. No se recomienda utilizarlo para scraping masivo sin autorización de las páginas web involucradas.
