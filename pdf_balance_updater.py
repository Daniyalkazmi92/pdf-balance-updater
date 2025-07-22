import pdfplumber
import pandas as pd
from fpdf import FPDF

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        table = first_page.extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    return df

def recalculate_balances(df, transaction_col, balance_col, starting_balance):
    balances = []
    current_balance = starting_balance
    for tx in df[transaction_col]:
        try:
            tx_value = float(tx.replace(',', '').replace('$', ''))
        except:
            tx_value = 0.0
        current_balance += tx_value
        balances.append(round(current_balance, 2))
    df[balance_col] = balances
    return df

def save_table_to_pdf(df, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    col_width = 190 / len(df.columns)

    # Header
    for col in df.columns:
        pdf.cell(col_width, 10, str(col), border=1)
    pdf.ln()

    # Rows
    for _, row in df.iterrows():
        for item in row:
            pdf.cell(col_width, 10, str(item), border=1)
        pdf.ln()

    pdf.output(output_path)
    print(f"New PDF saved as {output_path}")

# --------- Run the full workflow ---------
if __name__ == "__main__":
    input_pdf = "input.pdf"  # Replace with your file
    output_pdf = "output_updated.pdf"
    transaction_column = "Transaction"  # Column name in PDF
    balance_column = "Balance"          # Column to update
    starting_balance = 1000.00          # Set your starting balance

    df = extract_table_from_pdf(input_pdf)
    df = recalculate_balances(df, transaction_column, balance_column, starting_balance)
    save_table_to_pdf(df, output_pdf)
