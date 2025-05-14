import customtkinter as ctk
from PIL import Image, ImageTk

# Cada item: (imagem_path)
imagens_resultado = [
    {"azul": ("assets/resultados/resultado_azul.png")},
    {"amarelo": ("assets/resultados/resultado_vermelho.png")},
    {"vermelho": ("assets/resultados/resultado_amarelo.png")}
]

texto_procurar_profissiona = """
Consulte sempre um profissional da visão para um exame oftalmológico completo.
"""

class ResultadoView(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        # Configura linhas e colunas para centralizar tudo
        self.grid_rowconfigure(0, weight=1)  # Espaço acima
        self.grid_columnconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=0)
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_rowconfigure(2, weight=0)
        self.container.grid_rowconfigure(3, weight=0)
        self.container.grid_rowconfigure(4, weight=0)
        self.container.grid_rowconfigure(5, weight=1)
        self.container.grid_rowconfigure(6, weight=0)
        self.container.grid_rowconfigure(7, weight=0)
        self.container.grid_columnconfigure(0, weight=1)  

        self.carregar_resultado()         


    def carregar_resultado(self):       
        resultado = self.controller.resultado_do_exame
        
        # Título
        ctk.CTkLabel(
            self.container,
            text=resultado["titulo"],
            font=ctk.CTkFont(size=80, family='arial', weight="bold"),
            text_color="#222233",
            justify="center",
        ).grid(row=0, column=0, sticky="n")

        # Frame para as imagens dos olhos
        olhos_frame = ctk.CTkFrame(self.container, fg_color="white")
        olhos_frame.grid(row=2, column=0)

        olhos_frame.grid_columnconfigure((0, 1), weight=1)

        def obter_caminho_imagem(cor):
            for item in imagens_resultado:
                if cor in item:
                    return item[cor]
                
        # Olho esquerdo
        caminho_esquerdo = obter_caminho_imagem(resultado.get("olho_esquerdo", ""))
        if caminho_esquerdo:
            imagem_esquerda = Image.open(caminho_esquerdo).resize((150, 75))
            photo_esquerda = ImageTk.PhotoImage(imagem_esquerda)
            label_img_esquerda = ctk.CTkLabel(olhos_frame, image=photo_esquerda, text="")
            label_img_esquerda.image = photo_esquerda
            label_img_esquerda.grid(row=0, column=0, padx=40)            
            ctk.CTkLabel(
                olhos_frame,
                text="ESQUERDO",
                font=ctk.CTkFont(size=20),
                text_color="black"
            ).grid(row=1, column=0)

        # Olho direito
        caminho_direito = obter_caminho_imagem(resultado.get("olho_direito", ""))
        if caminho_direito:
            imagem_direita = Image.open(caminho_direito).resize((150, 75))
            photo_direita = ImageTk.PhotoImage(imagem_direita)
            label_img_direita = ctk.CTkLabel(olhos_frame, image=photo_direita, text="")
            label_img_direita.image = photo_direita
            label_img_direita.grid(row=0, column=1, padx=40)

            ctk.CTkLabel(
                olhos_frame,
                text="DIREITO",
                font=ctk.CTkFont(size=20),
                text_color="black"
            ).grid(row=1, column=1)

        # Mensagem
        ctk.CTkLabel(
            self.container,
            text=resultado["mensagem"],
            font=ctk.CTkFont(size=28, family="arial", weight="bold"),
            text_color="#36719f",
            justify="center",            
            wraplength=600
        ).grid(row=3, column=0, pady=(20, 10),sticky="n")

        # Texto para procurar um profissional
        ctk.CTkLabel(
            self.container,
            text=texto_procurar_profissiona,
            font=ctk.CTkFont(size=28, family='helvetica'),
            text_color="#222233",
            justify="center",
            wraplength=800
        ).grid(row=6, column=0, sticky="s")

        # Botão para voltar a home
        ctk.CTkButton(
            self.container,
            text="Voltar ao menu inicial",
            width=800,
            height=40,
            command= self.retornar_a_home()
        ).grid(row=7, sticky="s", pady=(10,30))

    def retornar_a_home(self):
        self.controller.switch("home")


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Resultado")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    class DummyController:
        resultado_do_exame = {
            "titulo": "Visão cromática",
            "mensagem": "A sua visão cromática parece ser boa",
            "olho_esquerdo": "azul",
            "olho_direito": "azul"
        }

        def switch(self, view_name):
            print(f"Switching to: {view_name}")

    app = ResultadoView(root, controller=DummyController())
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
