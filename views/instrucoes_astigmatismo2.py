import customtkinter as ctk
from PIL import Image


class InstrucoesAstigmatismoView2(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller  # instância de View
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        self.cards_data = {"icone": "assets/olho_direito_tapado.png", "titulo": "Está com os olhos prontos?", "descricao": "Tape o seu olho direito."}
        self.indice_atual = 0
        self.card_frame = None

        # Layout principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

        # Frame dos indicadores
        self.indicadores_frame = ctk.CTkFrame(self, fg_color="white")
        self.indicadores_frame.grid(row=1, column=0, pady=(0, 5))

        # Botão de próxima etapa
        self.botao_proximo = ctk.CTkButton(
            self,
            text="Próximo",
            command=self.concluir,
            font=ctk.CTkFont(size=22, weight="bold"),
            fg_color="#0078ff",
            hover_color="#005ccc",
            height=50,
            width=200
        )
        self.botao_proximo.grid(row=2, column=0, pady=10)

        self.mostrar_card(self.indice_atual)

    def mostrar_card(self, index):
        if self.card_frame:
            self.card_frame.destroy()

        self.card_frame = ctk.CTkFrame(self, fg_color="white")
        self.card_frame.grid(row=0, column=0, sticky="nsew")
        self.card_frame.grid_columnconfigure(0, weight=1)

        # Dividimos a área em linhas para centralização
        for i in range(7):
            self.card_frame.grid_rowconfigure(i, weight=1)

        dados = self.cards_data

        # Imagem
        img = Image.open(dados["icone"])
        img = img.resize((400, 200), Image.Resampling.LANCZOS)
        ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 200))

        ctk.CTkLabel(
            self.card_frame,
            image=ctk_image,
            text=""
        ).grid(row=2, column=0, pady=(10, 0), sticky="n")

        # Título
        ctk.CTkLabel(
            self.card_frame,
            text=dados["titulo"],
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color="#32373e"
        ).grid(row=3, column=0, pady=(0, 0), sticky="s")

        # Descrição
        ctk.CTkLabel(
            self.card_frame,
            text=dados["descricao"],
            font=ctk.CTkFont(size=30),
            wraplength=1500,
            justify="center",
            text_color="#696a76"
        ).grid(row=4, column=0, pady=(0, 0), padx=40, sticky="n")

        self.atualizar_indicadores()

    def atualizar_indicadores(self):
        for widget in self.indicadores_frame.winfo_children():
            widget.destroy()

        for i in range(1):
            cor = "#0078ff" if i == self.indice_atual else "lightgray"
            dot = ctk.CTkLabel(
                self.indicadores_frame,
                text="●",
                text_color=cor,
                font=ctk.CTkFont(size=20)
            )
            dot.pack(side="left", padx=2)

    def concluir(self):
        self.indice_atual = 0
        self.mostrar_card(self.indice_atual)
        self.controller.switch("astigmatismo2")

# Execução isolada
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Instruções do Teste de Visão")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = InstrucoesAstigmatismoView2(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()

