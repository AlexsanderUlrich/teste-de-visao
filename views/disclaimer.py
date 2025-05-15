from tkinter import Frame, Label, Button
import tkinter as tk


class DisclaimerView(Frame):
    def __init__(self, *args, controller=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=0, sticky="nsew")  # Garantir que ocupe toda a tela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        container = tk.Frame(self, bg="white")
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)  # Espaço acima        
        content_frame = tk.Frame(container, bg="white")
        content_frame.grid(row=0, column=0)

        texto_disclaimer = """ 
Este Teste de Visão Online serve para obter uma primeira impressão sobre o atual
desempenho da visão. Não é um exame médico e não dispensa a consulta de um
especialista para a prestação de cuidados oftalmológicos adequados. Não se
destina a ser utilizado no diagnóstico de doenças nem na sua mitigação,
tratamento ou prevenção. Este teste destina-se apenas a dar-lhe uma ideia geral da
sua acuidade visual e se é aconselhável realizar um exame oftalmológico por um
especialista. Recomendamos fazer um exame oftalmológico por um especialista de
dois em dois anos, ou mais cedo se constatar alterações na sua visão. A RSData
recusa qualquer responsabilidade por danos ou consequências decorrentes do Teste
de Visão Online e/ou das informações fornecidas.
"""

        # Título
        tk.Label(
            content_frame,
            text="Leia e aceite antes de começar.",
            font=("Roboto", 48, "bold"),
            fg="black",
            bg="white",
            justify="left"
        ).pack(pady=(10))

        # texto do disclaimer
        tk.Label(
            content_frame,
            text=texto_disclaimer,
            font=("Arial", 19),
            fg="gray",
            bg="white",
            justify="left",
        ).pack(pady=(10))
       

        # Botão de aceite
        tk.Button(
            content_frame,
            text="Aceito",
            font=("Helvetica", 24, "bold"),
            bg="white",
            fg="black",
            activebackground="#0078ff",
            activeforeground="white",
            relief="solid",
            borderwidth=1,
            pady=30,
            width=50
        ).pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    root.title("Teste de Visão")
    root.configure(bg="white")
    root.overrideredirect(True)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    Disclaimer_view = DisclaimerView(root)
    root.mainloop()