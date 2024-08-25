from data_table import TreeView
from enter import *
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
root.title("DB Interface")

style = sv_ttk
style.set_theme('dark')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill=tk.BOTH)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

notebook.add(frame1, text="Payments")
notebook.add(frame2, text="Company Info")
notebook.add(frame3, text="Insurance Policy")

table_info = TreeView(frame2, "company_info")
table_policy = TreeView(frame3, "InsurancePolicy")
table_payments = TreeView(frame1, "payments")


def fetch_data(tree, table, combo):
    query = f"SELECT * FROM {table} ORDER BY {combo}"
    connection = sqlite3.connect('database_name1.db')
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) != 0:
        tree.delete_rows()
        for row in rows:
            tree.insert_rows(row)
    connection.close()


def start_menu():
    show_payments()
    show_company_info()
    show_policy()


def show_payments():
    combo_payments = ttk.Combobox(frame1, state="readonly", values=["id", "company_id", "date", "amount"])
    combo_payments.pack()
    tk.Button(frame1, text="Sort", command=lambda: fetch_data(table_payments, "payments", combo_payments.get())).pack()
    table_payments.show()
    fetch_data(table_payments, "payments", "id")
    tk.Button(frame1, text="Add data", command=lambda: enter_window()).pack()


def show_company_info():
    combo_info = ttk.Combobox(frame2, state="readonly", values=["id", "name", "address", "phone"])
    combo_info.pack()
    tk.Button(frame2, text="Sort", command=lambda: fetch_data(table_info, "company_info", combo_info.get())).pack()
    table_info.show()
    fetch_data(table_info, "company_info", "id")
    tk.Button(frame2, text="Add data", command=lambda: enter_window()).pack()


def show_policy():
    combo_ins = ttk.Combobox(frame3, state="readonly", values=["PolicyID", "PolicyHolderName", "PolicyType",
                                                               "EffectiveDate", "ExpirationDate", "PremiumAmount",
                                                               "CompanyID"])
    combo_ins.pack()
    tk.Button(frame3, text="Sort", command=lambda: fetch_data(table_policy, "InsurancePolicy", combo_ins.get())).pack()
    table_policy.show()
    fetch_data(table_policy, "InsurancePolicy", "PolicyID")
    tk.Button(frame3, text="Add data", command=lambda: enter_window()).pack()


if __name__ == "__main__":
    start_menu()
    root.mainloop()


