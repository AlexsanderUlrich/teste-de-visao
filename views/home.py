from tkinter import Frame, Label, Button
import tkinter as tk


class HomeView(Frame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")  # Garantir que ocupe toda a tela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        container = tk.Frame(self, bg="#1c1c1c")
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)  # Espaço acima
        container.grid_rowconfigure(2, weight=1)  # Espaço abaixo
        
        content_frame = tk.Frame(container, bg="#1c1c1c")
        content_frame.grid(row=1, column=0)

        # Logo
        try:
            self.icon_img = tk.PhotoImage(file="assets/logo.png")
            tk.Label(content_frame, image=self.icon_img, bg="#1c1c1c").pack(pady=(0, 20))
        except Exception as e:
            print("Erro ao carregar imagem:", e)

        # Título
        tk.Label(
            content_frame,
            text="Teste de Visão\nRSData",
            font=("Roboto", 48, "bold"),
            fg="white",
            bg="#1c1c1c",
            justify="center"
        ).pack(pady=(0, 20))

        # Botão principal
        tk.Button(
            content_frame,
            text="Teste a sua visão",
            font=("Helvetica", 24, "bold"),
            bg="#0078ff",
            fg="white",
            activebackground="#005ccc",
            relief="flat",
            padx=20,
            pady=10,
            width=40
        ).pack(pady=(0, 10))

        # Botão secundário
        tk.Button(
            content_frame,
            text="Ou selecione um teste específico",
            font=("Helvetica", 24),
            bg="#1c1c1c",
            fg="white",
            activebackground="#333333",
            relief="solid",
            borderwidth=1,
            padx=20,
            pady=10,
            width=40,
            command=self.controller.ir_para_selecao
        ).pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    root.title("Teste de Visão")
    root.configure(bg="#1c1c1c")
    root.overrideredirect(True)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    home_view = HomeView(root)
    root.mainloop()