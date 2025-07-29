# 🕷️ Professional Web Scraper

This project is a tool for **automated professional scraping**, designed to extract product information from e-commerce websites that use dynamic content (JavaScript-rendered). The application automatically generates **reports in three formats**: `PDF`, `Excel`, and `JSON`, including the **product name, price, and image** for each available item.

> 🔎 This scraper has been successfully tested on the official website of [Tiendas D1](https://domicilios.tiendasd1.com/), specifically in the frozen food category.

---

## 📌 Main Features

| Functionality                         | Description |
|--------------------------------------|-------------|
| 🧠 Smart scraping                     | Uses `Selenium` to handle dynamic content. |
| 📦 Structured data extraction         | Extracts product name, price, and image. |
| 🧾 Multi-format reporting             | JSON, Excel (`.xlsx`), and PDF with embedded images. |
| 🛠️ Modular and extensible codebase   | Clear separation of logic into individual files. |
| 💡 Adaptable to multiple websites     | Support for modifying selectors and HTML structure. |

---

## 🚀 How does it work?

1. The user provides the URL of the page to scrape.
2. An automated browser (Edge or Brave) is launched using Selenium.
3. The script waits for the dynamic content (products) to load.
4. Relevant information is extracted using `BeautifulSoup`.
5. Three types of reports are automatically generated:
   - 📄 `report.pdf` with text and product images.
   - 📊 `report.xlsx` ready for analysis in Excel or Power BI.
   - 🧾 `report.json` containing structured data.

---

## 📁 Project Structure

```
web-scraper-app/
├── main.py              # Main script (orchestrates the process)
├── scraper.py           # Scraping and HTML parsing logic
├── reports.py           # Report generation (PDF, Excel, JSON)
├── requirements.txt     # Project dependencies
├── report.xlsx          # Generated Excel report
├── report.pdf           # PDF report with product images
├── report.json          # Structured data output
```

---

## 🔧 How to adapt it to other websites?

This scraper is **fully adaptable to other websites**, but you must understand the structure of their HTML. Follow these steps to customize it:

### 1. 🔍 Inspect the HTML of the target page

- Open your browser, right-click on a product, and select **"Inspect"**.
- Identify the **main container** for each product (e.g., `div.product-card`, `li.item`, etc.).
- Inside that container, locate:
  - **Product name**: Is it in a `<p>`, `<h2>`, `<span>`?
  - **Price**: Is it a `<p>`, `<div>`?
  - **Image**: Look for an `<img>` tag and extract the `src` attribute.

### 2. ✍️ Adjust the CSS selectors

The current selectors only work for Tiendas D1. For other websites, you’ll need to update:

- The class of the **product container**
- The tag and class where the **name** is located
- The tag and class where the **price** is located
- The location of the **image** (`<img>`) if available

> ⚠️ **Important:** Each selector should include both the **HTML tag** and the class, e.g.:  
> `p.product-name`, `div.price`, `img.product-image`.

### 3. ✅ Verify the extracted data

You can temporarily print the extracted products to the console with:

```python
print(products)
```

and check if everything looks correct before generating the reports.

---

## 🧪 Environment Requirements

- Python 3.8 or higher
- **Microsoft Edge** browser (recommended for Selenium compatibility)
- Google Chrome or Brave (also supported with minor adjustments)
- Required packages:
  - `selenium`
  - `bs4`
  - `requests`
  - `fpdf`
  - `pandas`
  - `openpyxl`
  - `webdriver-manager`
  - `Pillow`

---

## ⚙️ How to use the project

```bash
# Clone the repository
git clone https://github.com/JustBeingLuis/Web-Scraper-Profesional-.git
cd web-scraper-app

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python main.py
```

---

## 👨‍💻 Author

**Luis Toscano**  
Computer Science Student – UIS  
🔬 Project developed for research and portfolio purposes.  
Presented as part of professional web scraping practices.

---

## 📄 License

This project is free to use for educational purposes. It is not recommended for large-scale scraping without proper authorization from the websites involved.
