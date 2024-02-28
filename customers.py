from modules import *
from validentry import Validate
from reports import Reports
from functions import Funcs


class Application(Funcs, Reports, Validate):
    def __init__(self):
        self.root = root
        self.validainputs()
        self.screen()
        self.screen_frames()
        self.widgets()
        self.lower_frame()
        self.buildtable()
        self.select_list()
        self.menu()
        root.mainloop()

    def screen(self):
        self.root.title('Register Customer')
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')
        self.root.resizable('true', 'true')
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def screen_frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets(self):
        self.bt_clear = Button(self.frame_1, text='Clear', bd=2, bg='#107db2', fg='white', font=(
            'verdana', 8, 'bold'), command=self.clear_customer)
        self.bt_clear.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_search = Button(self.frame_1, text='Search', bd=2, bg='#107db2', fg='white', font=(
            'verdana', 8, 'bold'), command=self.search_customer)
        self.bt_search.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_new = Button(self.frame_1, text='New', bd=2, bg='#107db2', fg='white', font=(
            'verdana', 8, 'bold'), command=self.add_customer)
        self.bt_new.place(relx=0.56, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_edit = Button(self.frame_1, text='Edit', bd=2, bg='#107db2', fg='white', font=(
            'verdana', 8, 'bold'), command=self.edit_customer)
        self.bt_edit.place(relx=0.66, rely=0.1,
                           relwidth=0.1, relheight=0.15)
        self.bt_delete = Button(self.frame_1, text='Delete', bd=2, bg='#107db2', fg='white', font=(
            'verdana', 8, 'bold'), command=self.delete_customer)
        self.bt_delete.place(relx=0.76, rely=0.1, relwidth=0.1, relheight=0.15)
        self.lb_cod = Label(self.frame_1, text='Cod',
                            bg='#dfe3ee', fg='#107db2')
        self.lb_cod.place(relx=0.045, rely=0.05)
        self.cod_entry = Entry(
            self.frame_1, bg='#dfe3ee', fg='#107db2', validate="key", validatecommand=self.vcmd)
        self.cod_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        self.lb_name = Label(self.frame_1, text='Name',
                             bg='#dfe3ee', fg='#107db2')
        self.lb_name.place(relx=0.045, rely=0.3)
        self.name_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#107db2')
        self.name_entry.place(relx=0.05, rely=0.4, relwidth=0.8)
        self.lb_phone = Label(
            self.frame_1, text='Phone', bg='#dfe3ee', fg='#107db2')
        self.lb_phone.place(relx=0.045, rely=0.52)
        self.phone_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#107db2')
        self.phone_entry.place(relx=0.05, rely=0.62, relwidth=0.4)
        self.lb_city = Label(self.frame_1, text='City',
                             bg='#dfe3ee', fg='#107db2')
        self.lb_city.place(relx=0.495, rely=0.52)
        self.city_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#107db2')
        self.city_entry.place(relx=0.5, rely=0.62, relwidth=0.4)

    def lower_frame(self):
        self.listCus = ttk.Treeview(
            self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listCus.heading('#0', text='')
        self.listCus.heading('#1', text='Cod')
        self.listCus.heading('#2', text='Name')
        self.listCus.heading('#3', text='Phone')
        self.listCus.heading('#4', text='City')

        self.listCus.column('#0', width=1)
        self.listCus.column('#1', width=50)
        self.listCus.column('#2', width=200)
        self.listCus.column('#3', width=125)
        self.listCus.column('#4', width=125)

        self.listCus.place(relx=0, rely=0, relwidth=0.999, relheight=0.999)

        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.scroolList.place(relx=0.971, rely=0.008, relheight=0.985)
        self.listCus.configure(yscroll=self.scroolList.set)
        self.listCus.bind("<Double-1>", self.OnDoubleClick)

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)
        def Quit(): self.root.destroy()

        menubar.add_cascade(label="Settings", menu=filemenu)
        menubar.add_cascade(label="Reports", menu=filemenu2)

        filemenu2.add_command(label="Print form",
                              command=self.generate_report)
        filemenu.add_command(label="Sair", command=Quit)

    def validainputs(self):
        self.vcmd = (self.root.register(self.validate_entry_cod), '%P')


if __name__ == '__main__':
    root = Tk()
    Application()
