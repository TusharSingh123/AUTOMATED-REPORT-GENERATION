# Sales Report Generator 📊

A simple but powerful Sales Report Generator that reads sales data from a CSV file, summarizes it using Python's pandas library, and generates a clean, structured PDF report using the fpdf library. This tool is especially useful for small businesses, startups, freelancers, or anyone who needs to quickly analyze and present sales data in a professional format without using heavyweight software like Excel or BI tools.

## Features ✨

- ✅ Reads structured sales data (Name, Quantity, Price_per_unit) from a CSV file
- ✅ Automatically computes total revenue per entry (Quantity × Price)
- ✅ Summarizes total quantity and total revenue for each customer/product
- ✅ Generates a centered, well-aligned PDF report
- ✅ Adds a dynamic timestamp to the header
- ✅ Automatically handles missing or malformed data gracefully
- ✅ Uses system locale for proper currency formatting (₹ / $ / € etc.)
- ✅ Lightweight and easy to extend or customize

## File Structure 📁

```
├── sample_sales_data.csv      # Input CSV data
├── main.py                    # Main Python script
├── sales_report.pdf           # Output generated PDF
└── README.md                  # This documentation
```

## Requirements 🔧

To run this project, you'll need:

- Python 3.x
- pandas library
- fpdf library
- A valid CSV file with at least the following columns:
  - Name (string)
  - Quantity (integer)
  - Price_per_unit (float or integer)

### Installation

Install the required dependencies:

```bash
pip install pandas fpdf
```

## Input Format 📥

The input should be a CSV file (e.g., `sample_sales_data.csv`) with at least the following columns:

```csv
Name,Quantity,Price_per_unit
John,3,100
Alice,2,150
John,1,100
```

## Output 📤

The script generates a PDF file (`sales_report.pdf`) that includes:

- A title: "Sales Report"
- The date and time of generation
- A table with:
  - Name
  - Total Quantity
  - Total Revenue (formatted as currency)
- Page number as a footer
- All content is centered and professionally formatted

## How It Works 🧠

1. The script reads the CSV data using pandas
2. It checks for necessary columns (Name, Quantity, Price_per_unit)
3. It computes a new column `Total_Price = Quantity * Price_per_unit`
4. It groups the data by Name and calculates total quantity and total revenue
5. The data is passed to the fpdf-based class, which:
   - Creates a formatted PDF page
   - Adds headers and footers
   - Calculates total table width and dynamically centers it
   - Adds rows and formats revenue using locale-specific currency
6. Finally, the PDF is saved as `sales_report.pdf`

## Customization Ideas 🔄

You can easily extend this project:

- Add charts (e.g., pie chart or bar chart of top customers)
- Add a company logo in the header
- Include product names, categories, or invoice numbers
- Generate monthly/weekly reports using filters
- Email the PDF directly using smtplib

## Best Practices Followed ✅

- Error handling during file reading and missing columns
- Modular functions for separation of logic
- Dynamic layout for responsive and neat PDFs
- System locale for global compatibility
- Clean, readable code with comments and structure

## Use Cases 📈

- 🧾 Generating client invoices
- 📊 Monthly/weekly sales reporting
- 📦 E-commerce order summaries
- 🛒 Marketplace analytics
- 🧑‍💻 College project on data visualization
- 💼 Portfolio/demo for PDF automation skills

## Contributing 📬

If you'd like to contribute improvements or features, feel free to fork the repo and open a pull request. You can also contact me with feedback, suggestions, or collaboration ideas.

## Disclaimer ⚠️

This project is a template and should be used for educational or lightweight reporting purposes. For enterprise-grade reporting, consider integrating with full-fledged reporting platforms like ReportLab, LaTeX, or Tableau.

---

*Built with Python, pandas, and fpdf*
