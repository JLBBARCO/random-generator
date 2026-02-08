import random
import customtkinter as ctk

padMain = 10

# Armazenamento em nível de módulo para que chamadores possam ler `randomNumbers.numbers`
numbers = []

def randomNumbers(quantity, min_num=0, max_num=100):
    """Gera `quantity` inteiros aleatórios entre min_num e max_num.
    A lista gerada é armazenada na variável de módulo `numbers` e também
    como atributo da função `randomNumbers.numbers` (compatibilidade).
    Retorna a lista gerada.
    """
    global numbers
    try:
        qty = int(quantity)
    except (TypeError, ValueError):
        qty = 0

    if qty < 1:
        numbers = []
        randomNumbers.numbers = numbers
        return numbers

    # garante que min < max
    try:
        min_v = int(min_num)
        max_v = int(max_num)
    except (TypeError, ValueError):
        min_v = 0
        max_v = 100

    if min_v > max_v:
        min_v, max_v = max_v, min_v

    gen = []
    for i in range(qty):
        gen.append((i, random.randint(min_v, max_v)))

    numbers = gen
    randomNumbers.numbers = numbers
    return numbers

class RandomNumbersDialog(ctk.CTkToplevel):
    """Janela opcional para geração de números (não usada pelo main.py por padrão).
    Implementação mínima funcional: lê entradas, chama `randomNumbers` e fecha.
    """
    def __init__(self):
        super().__init__()
        self.title('Random Numbers')
        self.resizable(False, False)
        self.geometry('400x250')

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, width=380, height=230)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Title
        self.titleLabel = ctk.CTkLabel(self.main_frame, text='Random Numbers', font=('Arial', 14, 'bold'))
        self.titleLabel.pack(padx=padMain, pady=padMain)

        self.inputQuantity = ctk.CTkEntry(self.main_frame, placeholder_text='Quantity of Numbers')
        self.inputQuantity.pack(padx=padMain, pady=padMain)
        self.inputMinNumbers = ctk.CTkEntry(self.main_frame, placeholder_text='Min of Numbers')
        self.inputMinNumbers.pack(padx=padMain, pady=padMain)
        self.inputMaxNumbers = ctk.CTkEntry(self.main_frame, placeholder_text='Max of Numbers')
        self.inputMaxNumbers.pack(padx=padMain, pady=padMain)

        # Frame for buttons
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(padx=padMain, pady=10)

        self.submitButton = ctk.CTkButton(button_frame, text='Submit', command=self.submit, width=100)
        self.submitButton.pack(side='left', padx=5)

        self.cancelButton = ctk.CTkButton(button_frame, text='Cancel', command=self.destroy, width=100)
        self.cancelButton.pack(side='left', padx=5)

    def submit(self):
        """Lê os valores dos campos, chama a função de geração e fecha a janela."""
        try:
            qty = int(self.inputQuantity.get())
        except (TypeError, ValueError):
            qty = 0

        try:
            min_v = int(self.inputMinNumbers.get())
        except (TypeError, ValueError):
            min_v = 0

        try:
            max_v = int(self.inputMaxNumbers.get())
        except (TypeError, ValueError):
            max_v = 100

        randomNumbers(qty, min_v, max_v)
        self.destroy()