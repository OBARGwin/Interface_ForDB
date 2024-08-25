import tkinter as tk
from tkinter import messagebox
import sqlite3
import sv_ttk


def enter_data(window, polisid_entry, pholdername_entry, polistype_entry, efdate_entry, exdate_entry, company_id_entry,
               company_name_entry, company_address_entry, company_phone_entry, pre_amount_entry, single_entry,
               comp_id_entry, amount_entry, date_entry):
    polisid = polisid_entry.get()
    pholdername = pholdername_entry.get()
    polistype = polistype_entry.get()
    efdate = efdate_entry.get()
    exdate = exdate_entry.get()
    company_id = company_id_entry.get()
    company_name = company_name_entry.get()
    company_address = company_address_entry.get()
    company_phone = company_phone_entry.get()
    pre_amount = pre_amount_entry.get()
    single_id = single_entry.get()
    comp_id = comp_id_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()

    flag = single_id.isdigit() and comp_id.isdigit() and amount.isdigit and date

    if (polisid.isdigit() and pholdername and polistype and efdate and exdate and pre_amount.isdigit()
        and company_id.isdigit() and company_name and company_address and company_phone) or flag:
        print(single_id, comp_id, amount, date)
        if flag:
            conn = sqlite3.connect('database_name1.db')
            data_insert_query_pay = '''INSERT INTO payments (id, company_id, amount, date) VALUES(?,?,?,?)'''
            data_insert_tuple_pay = (single_id, comp_id, amount, date)
            cursor = conn.cursor()
            cursor.execute(data_insert_query_pay, data_insert_tuple_pay)
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect('database_name1.db')
            data_insert_query = '''INSERT INTO InsurancePolicy (PolicyId, PolicyHolderName, PolicyType, EffectiveDate,
             ExpirationDate, PremiumAmount) VALUES(?,?,?,?,?,?)'''
            data_insert_tuple = (polisid, pholdername, polistype, efdate, exdate, pre_amount)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            data_insert_query1 = '''INSERT INTO company_info (id, name, address, phone) VALUES (?,?,?,?)'''
            data_insert_tuple1 = (company_id, company_name, company_address, company_phone)
            cursor = conn.cursor()
            cursor.execute(data_insert_query1, data_insert_tuple1)
            conn.commit()
            conn.close()
        close(window)

    else:
        tk.messagebox.showwarning(title="Error", message="Error, mustn't be null or datatype isn't correct!")


def enter_window():
    wind = tk.Tk()
    wind.geometry("900x400")
    wind.title("DB Interface")

    frame = tk.Frame(wind)
    frame.pack()

    insur_info_frame = tk.LabelFrame(frame, text="InsurancePolis")
    insur_info_frame.grid(row=0, column=0, padx=10, pady=10)

    polisid_label = tk.Label(insur_info_frame, text="PolisID")
    polisid_label.grid(row=0, column=0)
    polisid_entry = tk.Entry(insur_info_frame)
    polisid_entry.grid(row=1, column=0)

    pholdername_label = tk.Label(insur_info_frame, text="PolisHolderName")
    pholdername_label.grid(row=0, column=1)
    pholdername_entry = tk.Entry(insur_info_frame)
    pholdername_entry.grid(row=1, column=1)

    polistype_label = tk.Label(insur_info_frame, text="PolisType")
    polistype_label.grid(row=0, column=2)
    polistype_entry = tk.Entry(insur_info_frame)
    polistype_entry.grid(row=1, column=2)

    efdate_label = tk.Label(insur_info_frame, text="EffectiveDate")
    efdate_label.grid(row=0, column=3)
    efdate_entry = tk.Entry(insur_info_frame)
    efdate_entry.grid(row=1, column=3)

    exdate_label = tk.Label(insur_info_frame, text="ExpirationDate")
    exdate_label.grid(row=0, column=4)
    exdate_entry = tk.Entry(insur_info_frame)
    exdate_entry.grid(row=1, column=4)

    pre_amount_label = tk.Label(insur_info_frame, text="PremiumAmount")
    pre_amount_label.grid(row=0, column=5)
    pre_amount_entry = tk.Entry(insur_info_frame)
    pre_amount_entry.grid(row=1, column=5)

    for widget in insur_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    company_info_frame = tk.LabelFrame(frame, text="companyinfo")
    company_info_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

    company_id_label = tk.Label(company_info_frame, text="CompanyId")
    company_id_label.grid(row=1, column=0)
    company_id_entry = tk.Entry(company_info_frame)
    company_id_entry.grid(row=2, column=0)

    company_name = tk.Label(company_info_frame, text="CompanyName")
    company_name.grid(row=1, column=1)
    company_name_entry = tk.Entry(company_info_frame)
    company_name_entry.grid(row=2, column=1)

    company_address = tk.Label(company_info_frame, text="CompanyAddress")
    company_address.grid(row=1, column=2)
    company_address_entry = tk.Entry(company_info_frame)
    company_address_entry.grid(row=2, column=2)

    company_phone = tk.Label(company_info_frame, text="CompanyPhone")
    company_phone.grid(row=1, column=3)
    company_phone_entry = tk.Entry(company_info_frame)
    company_phone_entry.grid(row=2, column=3)

    for widget in company_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    payments_frame = tk.LabelFrame(frame, text="Payments")
    payments_frame.grid(row=2, column=0, sticky="news", padx=10, pady=10)

    single_id = tk.Label(payments_frame, text="ID")
    single_id.grid(row=2, column=0)
    single_id_enter = tk.Entry(payments_frame)
    single_id_enter.grid(row=3, column=0)

    comp_id = tk.Label(payments_frame, text="CompanyID")
    comp_id.grid(row=2, column=1)
    comp_id_enter = tk.Entry(payments_frame)
    comp_id_enter.grid(row=3, column=1)

    amount = tk.Label(payments_frame, text="Amount")
    amount.grid(row=2, column=2)
    amount_entry = tk.Entry(payments_frame)
    amount_entry.grid(row=3, column=2)

    date = tk.Label(payments_frame, text="Date")
    date.grid(row=2, column=3)
    date_entry = tk.Entry(payments_frame)
    date_entry.grid(row=3, column=3)

    for widget in payments_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = tk.Button(frame, text="Enter data", command=lambda: enter_data(wind, polisid_entry, pholdername_entry,
                                                                            polistype_entry, efdate_entry,
                                                                            exdate_entry, company_id_entry,
                                                                            company_name_entry, company_address_entry,
                                                                            company_phone_entry, pre_amount_entry,
                                                                            single_id_enter, comp_id_enter,
                                                                            amount_entry, date_entry))
    button.grid(row=3, column=0, sticky="news", padx=10, pady=10)

    wind.mainloop()


def close(window):
    window.destroy()
