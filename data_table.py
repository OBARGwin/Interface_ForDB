from tkinter import ttk, Menu


class TreeView:
    def __init__(self, window, table):
        self.start_width = None
        self.column = None
        self.initial_x = None
        columns_dict = {
            "payments": [("id", "ID"), ("company_id", "Company_id"), ("amount", "Amount"), ("date", "Date")],
            "company_info": [("id", "ID"), ("name", "Company_name"), ("address", "Address"), ("phone", "Phone")],
            "InsurancePolicy": [("Policy_ID", "Policy_ID"), ("PolicyHolderName", "PolicyHolderName"),
                                ("PolicyType", "PolicyType"), ("EffectiveDate", "EffectiveDate"),
                                ("ExpirationDate", "ExpirationDate"), ("PremiumAmount", "PremiumAmount"),
                                ("CompanyID", "CompanyID")]
        }
        columns = columns_dict.get(table)
        if columns:
            self.tree = ttk.Treeview(window, columns=[col[0] for col in columns], show="headings")
            for col_name, col_heading in columns:
                self.tree.heading(col_name, text=col_heading)
                self.tree.column(col_name, stretch=True)  # Разрешает изменение размера столбца
                self.tree.column(col_name, width=100)  # Начальная ширина столбца

            # Добавляем возможность изменять размер столбцов с помощью мыши
            self.tree.bind("<ButtonRelease-1>", self.start_resize)

        self.context_menu = Menu(self.tree, tearoff=0)
        self.context_menu.add_command(label="Delete", command=self.delete_row)

        # Bind the context menu to the right-click event
        self.tree.bind("<Button-3>", self.popup)

    def start_resize(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if "separator" in region:
            self.tree.config(cursor="sb_h_double_arrow")  # Меняем курсор при наведении на разделитель столбцов
            self.initial_x = event.x
            self.column = self.tree.identify_column(event.x)
            self.start_width = self.tree.column(self.column, "width")
            self.tree.bind("<B1-Motion>", self.resize)
            self.tree.bind("<ButtonRelease-1>", self.stop_resize)
            
    def resize(self, event):
        delta = event.x - self.initial_x
        new_width = self.start_width + delta
        self.tree.column(self.column, width=new_width)

    def stop_resize(self, event):
        self.tree.config(cursor="")
        self.tree.unbind("<B1-Motion>")

    def show(self):
        self.tree.pack(fill="x", pady=10)

    def delete_rows(self):
        children = self.tree.get_children()
        for child in children:
            self.tree.delete(child)
            
    def insert_rows(self, row):
        self.tree.insert('', 'end', values=row)

    def popup(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            print("No row selected.")
