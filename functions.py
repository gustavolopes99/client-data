from modules import *


class Funcs():
    def clear_customer(self):
        self.cod_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.city_entry.delete(0, END)

    def conect_db(self):
        self.conn = sqlite3.connect('customers.db')
        self.cur = self.conn.cursor()

    def desconnect_bd(self):
        self.conn.close()

    def buildtable(self):

        self.conect_db()
        print("Connecting data")
        self.cur.execute("""
                                CREATE TABLE IF NOT EXISTS 
                                                TCUSTOMERS (                         
                                cod INTEGER PRIMARY KEY,
                                name_customer CHAR(40) NOT NULL,
                                phone INTEGER(20),
                                city CHAR(40)
                                );
                                """)
        self.conn.commit()
        print("Database created!")
        self.desconnect_bd()
        print('!')

    def variable(self):
        self.cod = self.cod_entry.get()
        self.name = self.name_entry.get()
        self.phone = self.phone_entry.get()
        self.city = self.city_entry.get()

    def add_customer(self):
        self.variable()
        self.conect_db()
        self.cur.execute("""INSERT INTO TCUSTOMERS (name_customer, phone, city)
                                                                        values
                                                    (?, ?, ?)""", (self.name, self.phone, self.city))
        self.conn.commit()
        self.conn.close()
        self.clear_customer()
        self.select_list()

    def select_list(self):
        self.listCus.delete(*self.listCus.get_children())
        self.conect_db()
        getlist = self.cur.execute("""SELECT 
                                        cod, 
                                        name_customer, 
                                        phone, 
                                        city 
                                FROM TCUSTOMERS
                                        ORDER BY name_customer ASC""")
        for i in getlist:
            self.listCus.insert("", END, values=i)
        self.desconnect_bd()

    def OnDoubleClick(self, event):
        self.clear_customer()
        self.listCus.selection()
        for n in self.listCus.selection():
            col1, col2, col3, col4 = self.listCus.item(n, 'values')
            self.cod_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.phone_entry.insert(END, col3)
            self.city_entry.insert(END, col4)

    def delete_customer(self):
        self.variable()
        self.conect_db()
        try:
            self.cur.execute("""DELETE FROM 
                                        TCUSTOMERS WHERE cod = ?""", (self.cod))
            self.conn.commit()
            print("Data removed!")
        except sqlite3.ProgrammingError as e:
            messagebox.showwarning(
                'Warning', 'No customer.')
        self.desconnect_bd()
        self.clear_customer()
        self.select_list()

    def edit_customer(self):
        self.variable()
        self.conect_db()
        self.cur.execute("""UPDATE 
                                TCLIENTES SET 
                                            nome_cliente = ?,
                                            telefone = ?,
                                            cidade = ?
                                where
                                            cod = ?""", (self.name, self.phone, self.city, self.codigo))
        self.conn.commit()
        self.desconnect_bd()
        self.select_list()
        self.clear_customer()

    def search_customer(self):
        self.conect_db()
        self.listCus.delete(*self.listCus.get_children())
        self.name_entry.insert(END, '%')
        name = self.name_entry.get()
        self.cur.execute("""SELECT 
                                    COD, 
                                    NAME_CUSTOMER, 
                                    PHONE, 
                                    CITY 
                                        FROM TCUSTOMERS WHERE 
                                    TCUSTOMERS.NAME_CUSTOMER LIKE '%s' order by TCUSTOMERS.NAME_CUSTOMER """ % name)
        findnameCus = self.cur.fetchall()
        for i in findnameCus:
            self.listCus.insert("", END, values=i)
        self.clear_customer()
        self.desconnect_bd()
