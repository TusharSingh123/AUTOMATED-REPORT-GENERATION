from fpdf import FPDF
import pandas as pd
import locale
from datetime import datetime

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, '')

# Load and validate data
def load_and_process_data(file_path):
    try:
        df = pd.read_csv(file_path)
        required_columns = {"Name", "Quantity", "Price_per_unit"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")
        
        df["Total_Price"] = df["Quantity"] * df["Price_per_unit"]
        summary = df.groupby("Name", as_index=False).agg({
            "Quantity": "sum",
            "Total_Price": "sum"
        })
        return summary
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Sales Report", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create PDF Report
def generate_pdf(summary, filename="sales_report.pdf"):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Table headers
    pdf.set_fill_color(200, 220, 255)
    headers = [("Name", 60), ("Total Quantity", 40), ("Total Revenue", 60)]
    for header, width in headers:
        pdf.cell(width, 10, header, 1, 0, 'C', fill=True)
    pdf.ln()

    # Table rows
    for _, row in summary.iterrows():
        pdf.cell(60, 10, str(row["Name"]), 1)
        pdf.cell(40, 10, str(int(row["Quantity"])), 1, align='C')
        formatted_price = locale.currency(row["Total_Price"], grouping=True)
        pdf.cell(60, 10, formatted_price, 1, 1, align='R')

    # Save the file
    pdf.output(filename)
    print(f"Report generated: {filename}")

# Main Execution
if __name__ == "__main__":
    summary_data = load_and_process_data("sample_sales_data.csv")
    if not summary_data.empty:
        generate_pdf(summary_data)
