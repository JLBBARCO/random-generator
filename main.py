import subprocess
subprocess.run(["src\lib\install.bat"], shell=True)
import customtkinter as ctk

padMain = 10
simpleGeometry = '360x120'
compostGeometry = '360x350'

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Random Generator')
        self.geometry(simpleGeometry)

        self.main_frame = ctk.CTkFrame(self, width=350, height=150)
        self.main_frame.grid(row=0, column=0, padx=padMain, pady=padMain)

        self.textTitle = ctk.CTkLabel(self.main_frame, text='Random Generator')
        self.textTitle.grid(row=0, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.buttonNumber = ctk.CTkButton(self.main_frame, text='Random Number', command=self.randomNumber)
        self.buttonNumber.grid(row=1, column=0, padx=padMain, pady=padMain)

        self.buttonName = ctk.CTkButton(self.main_frame, text='Random Name', command=self.randomName)
        self.buttonName.grid(row=1, column=2, padx=padMain, pady=padMain)

        self.printArea = ctk.CTkFrame(self, width=250, height=150)

    def show_error(self, message):
        """Mostra uma mensagem de erro na área de impressão."""
        self.geometry(compostGeometry)
        self.printArea.destroy()
        self.printArea = ctk.CTkFrame(self, width=250, height=150)
        self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)
        err = ctk.CTkLabel(self.printArea, text=message)
        err.grid(row=0, column=0, padx=padMain, pady=padMain)

    def randomNumber(self):
        dialog = ctk.CTkInputDialog(title='Random Number', text='Input the quantity of numbers generated')
        value = dialog.get_input()

        self.geometry(compostGeometry)

        import src.lib.random_numbers as random_numbers

        if value is None:
            # usuário cancelou
            return

        try:
            qty = int(value)
        except (TypeError, ValueError):
            self.show_error('Entrada inválida: informe um número inteiro')
            return

        if qty < 1:
            self.show_error('Quantidade deve ser >= 1')
            return

        # Gera números e usa a lista armazenada no módulo
        random_numbers.randomNumbers(qty)
        numbers = getattr(random_numbers, 'numbers', [])

        self.printArea.destroy()
        self.printArea = ctk.CTkScrollableFrame(self, width=250, height=150)
        self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

        for c, n in numbers:
            item = ctk.CTkLabel(self.printArea, text=str(n))
            item.grid(row=c, column=0, padx=padMain, pady=padMain)

    def randomName(self):
        dialog = ctk.CTkInputDialog(title='Random Name', text='Input the quantity of names generated')
        value = dialog.get_input()

        import src.lib.random_names as random_names

        self.geometry(compostGeometry)

        if value is None:
            return

        try:
            qty = int(value)
        except (TypeError, ValueError):
            self.show_error('Entrada inválida: informe um número inteiro')
            return

        if qty < 1:
            self.show_error('Quantidade deve ser >= 1')
            return

        random_names.randomNames(qty)
        names = getattr(random_names, 'names', [])

        self.printArea.destroy()
        self.printArea = ctk.CTkScrollableFrame(self, width=250, height=150)
        self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

        for c, n in names:
            item = ctk.CTkLabel(self.printArea, text=str(n))
            item.grid(row=c, column=0, padx=padMain, pady=padMain)


if __name__ == '__main__':
    app = App()
    app.mainloop()