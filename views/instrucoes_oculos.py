import customtkinter as ctk
from PIL import Image

class InstrucoesView(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        # Layout da página toda expansível
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)      

        # Lista de cards
        self.adicionar_cards([
            {"icone": "assets/oculos_lente.png", "titulo": "Esteja preparado(a)", "descricao": "Coloque os seus óculos ou lentes de contacto (se usar)."},
        ])

    # Criação do estilo do componente Card
    def criar_card(self, parent, card_data):

        # Criando o card
        card_frame = ctk.CTkFrame(parent, fg_color="white", width=600, height=400)
        card_frame.place(x=0, y=0)        
        #card_frame.grid_propagate(False)  # Impede que o card se ajuste ao conteúdo
        card_frame.grid_columnconfigure(0, weight=0)

        # Imagem do card
        image_path = card_data.get("icone")
        if image_path:
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(300, 250))
            ctk.CTkLabel(card_frame, image=ctk_image, text="").grid(row=0, column=0, pady=(10, 0), sticky="ns")

        # Título
        ctk.CTkLabel(card_frame, text=card_data.get("titulo"), font=ctk.CTkFont(size=45, family='Roboto', weight="bold"), text_color="#32373e").grid(row=3, column=0)

        # Descrição
        ctk.CTkLabel(card_frame,text=card_data.get("descricao"),font=ctk.CTkFont(size=40, family='helvetica'),wraplength=800,justify="center", text_color="gray"
        ).grid(row=4, column=0, pady=(5, 10), padx=10, sticky="n")            

        return card_frame
    
    # Funções de estrutura
    def adicionar_cards(self, lista_de_cards):
        for i, card_data in enumerate(lista_de_cards):
            card = self.criar_card(self, card_data)
            card.grid(row=i, column=0, pady=10, padx=20, sticky="n")

# Execução isolada
if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # ou "dark"
    root = ctk.CTk()
    root.title("Teste de Visão - Seleção")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = InstrucoesView(root)
    app.grid(sticky="nsew")

    # Ativar maximização após o layout estar pronto
    root.after(100, lambda: root.state("zoomed"))
    root.overrideredirect(True)
    root.mainloop()
