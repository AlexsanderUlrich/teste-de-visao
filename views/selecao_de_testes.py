import customtkinter as ctk
from PIL import Image


class SelecaoDeTestesView(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller  # instância de View
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self,
            text="Escolha um dos nossos \ntestes para começar",
            font=ctk.CTkFont("Helvetica", 50, "bold"),
            text_color="black",
            fg_color="white"
        ).grid(row=0, column=0, sticky="ew", pady=(20, 10))

        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="white", width=760)
        self.scroll_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        self.scroll_frame.bind("<Enter>", self._ativar_scroll)
        self.scroll_frame.bind("<Leave>", self._desativar_scroll)

        self.adicionar_cards([
            {
                "icone": "assets/abertura_icone.png",
                "titulo": "Encontre a abertura",
                "descricao": "Verifique a nitidez da sua visão com o nosso teste de acuidade visual.",
                "view": "abertura"
            },
            {
                "icone": "assets/daltonismo_icone.png",
                "titulo": "Olhe para o arco-íris.",
                "descricao": "Consegue distinguir claramente as cores? O nosso teste da visão cromática vai determinar até que ponto.",
                "view": "instrucoesDaltonismo"
            },
            {
                "icone": "assets/olhePonto_icone.png",
                "titulo": "Olhe para o ponto",
                "descricao": "O teste do campo visual consegue detetar problemas com o seu campo visual.",
                "view": "campo_visual"
            }
        ])

    def criar_card(self, parent, card_data):
        card_frame = ctk.CTkFrame(
            parent,
            fg_color="white",
            width=500,
            height=350,
            corner_radius=20,
            border_width=1,
            border_color="#0078ff"
        )
        card_frame.place(x=0, y=0)
        card_frame.grid_propagate(False)
        card_frame.grid_columnconfigure(0, weight=1)

        image_path = card_data.get("icone")
        if image_path:
            img = Image.open(image_path)
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(70, 70))
            ctk.CTkLabel(card_frame, image=ctk_image, text="").grid(row=0, column=0, pady=(10, 0), sticky="ns")

        ctk.CTkLabel(
            card_frame,
            text=card_data.get("titulo", "Título"),
            font=ctk.CTkFont(size=30, family='Helvetica', weight="bold")
        ).grid(row=1, column=0)

        ctk.CTkLabel(
            card_frame,
            text=card_data.get("descricao", "Descrição do teste."),
            font=ctk.CTkFont(size=20, family='helvetica'),
            wraplength=460,
            justify="center"
        ).grid(row=2, column=0, pady=(5, 10), padx=10, sticky="n")

        def button_event():
            if self.controller:
                self.controller.switch(card_data["view"])

        ctk.CTkButton(
            card_frame,
            text="Iniciar Teste",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="#0078ff",
            hover_color="#005ccc",
            height=40,
            width=200,
            command=button_event
        ).grid(row=3, column=0, pady=(5, 20), padx=10, sticky="s")

        return card_frame

    def adicionar_cards(self, lista_de_cards):
        for i, card_data in enumerate(lista_de_cards):
            card = self.criar_card(self.scroll_frame, card_data)
            card.grid(row=i, column=0, pady=10, padx=20, sticky="n")

    def _ativar_scroll(self, event):
        self.scroll_frame.bind("<MouseWheel>", self._scroll_mouse)

    def _desativar_scroll(self, event):
        self.scroll_frame.unbind("<MouseWheel>")

    def _scroll_mouse(self, event):
        self.scroll_frame._parent_canvas.yview_scroll(int(-50 * (event.delta / 120)), "units")


# Execução isolada para testes locais
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Seleção")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = SelecaoDeTestesView(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.overrideredirect(True)
    root.mainloop()
