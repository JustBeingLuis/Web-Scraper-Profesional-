# reports.py
import pandas as pd
from fpdf import FPDF
import json

def generate_excel_report(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def generate_pdf_report(data, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Informe de Productos", ln=True, align="C")
    pdf.ln(10)
    for item in data:
        pdf.cell(0, 10, f"Nombre: {item['nombre']} - Precio: {item['precio']}", ln=True)
    pdf.output(filename)

def generate_json_report(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)