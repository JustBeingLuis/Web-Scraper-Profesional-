# main.py
from scraper import fetch_html, parse_products
from reports import generate_excel_report, generate_pdf_report, generate_json_report

def main():
    url = input("Ingresa la URL de la página a scrapear: ")
    html = fetch_html(url)
    productos = parse_products(html)  # Aquí se extraen los datos
    print(f"Productos extraídos: {productos}")

    generate_excel_report(productos, "informe.xlsx")
    generate_pdf_report(productos, "informe.pdf")
    generate_json_report(productos, "informe.json")
    print("¡Informes generados!")

if __name__ == "__main__":
    main()