# pdf-balance-updater
 A simple Python script to extract a table from a PDF, recalculate the "Balance" column using transaction amounts and a starting balance, and generate a new PDF with updated values.
 # 🧾 PDF Transaction Table Updater

This Python script reads a table from a PDF (using `pdfplumber`), recalculates transaction balances, and saves the updated table into a new PDF (using `FPDF`). Ideal for updating financial reports, bank statements, or ledger entries.

---

## 📌 Features

- Extracts tables from the **first page** of a PDF
- Parses transaction values and updates a **running balance**
- Saves the updated table into a new clean PDF
- Supports currency-formatted values like `$1,200.00`

---

## 🛠️ Technologies Used

- `pdfplumber` – Extract tables from PDFs
- `pandas` – Handle tabular data
- `fpdf` – Create and export to PDF

---

## 🚀 How to Use

### 🔧 1. Install Dependencies

```bash
pip install pdfplumber pandas fpdf
```

### 📁 2. Place your input PDF

Make sure your PDF file is in the same directory and has a valid table on the first page.

### 📝 3. Update Script Parameters (optional)

```python
input_pdf = "input.pdf"
output_pdf = "output_updated.pdf"
transaction_column = "Transaction"
balance_column = "Balance"
starting_balance = 1000.00
```

### ▶️ 4. Run the Script

```bash
python your_script_name.py
```

---

## 📤 Output

A new PDF file (`output_updated.pdf`) will be generated containing the updated balance column based on your transactions.

---

## 📂 Example Table Format

| Date       | Description     | Transaction | Balance |
|------------|------------------|-------------|---------|
| 01-01-2024 | Opening Balance | $0.00       | 1000.00 |
| 02-01-2024 | Payment         | -$100.00    | 900.00  |
| 03-01-2024 | Refund          | $50.00      | 950.00  |

---

## 🧠 Notes

- Make sure the PDF has an **extractable table** (i.e. not just an image).
- If the column names differ, update `transaction_column` and `balance_column` variables accordingly.
- Currency symbols and commas are handled automatically.

---

## 📄 License

This script is provided under the MIT License.

