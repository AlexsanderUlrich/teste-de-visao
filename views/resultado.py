import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from . import daltonismo
from . import exame_ponto2
from . import astigmatismo2
from . import acuidade2


# Cada item: (imagem_path)
imagens_resultado = [
    {"azul": "assets/resultados/resultado_azul.png"},
    {"amarelo": "assets/resultados/resultado_amarelo.png"},
    {"vermelho": "assets/resultados/resultado_vermelho.png"}
]

texto_procurar_profissiona = """
Consulte sempre um profissional da visão para um exame oftalmológico completo.
"""

resultado = {
    "titulo": "",
    "mensagem": "",
    "olho_esquerdo": "",
    "olho_direito": ""
}

class ResultadoView(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        # Configura linhas e colunas para centralizar tudo
        self.grid_rowconfigure(0, weight=1)
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
        global resultado
        print("Resultado do teste de daltonismo: ", daltonismo.resultado)
        print("Resultado do teste do campo de visão: ", exame_ponto2.resultado)
        print("Resultado do teste de astigmatismo: ", astigmatismo2.resultado)
        print("Resultado do teste de acuidade: ", acuidade2.resultado)
        print(resultado)

        if daltonismo.resultado != {}:
            resultado = daltonismo.resultado
        elif exame_ponto2.resultado != {}:
            resultado = exame_ponto2.resultado
        elif astigmatismo2.resultado != {}:
            resultado = astigmatismo2.resultado
        elif acuidade2.resultado != {}:
            resultado = acuidade2.resultado

        # Título
        ctk.CTkLabel(
            self.container,
            text=resultado["titulo"],
            font=ctk.CTkFont(size=28, family='arial', weight="bold"),
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
            photo_esquerda = CTkImage(light_image=imagem_esquerda, size=(150, 75))
            ctk.CTkLabel(olhos_frame, image=photo_esquerda, text="").grid(row=0, column=0, padx=40)
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
            photo_direita = CTkImage(light_image=imagem_direita, size=(150, 75))
            ctk.CTkLabel(olhos_frame, image=photo_direita, text="").grid(row=0, column=1, padx=40)
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
            font=ctk.CTkFont(size=50, family="arial", weight="bold"),
            text_color="#36719f",
            justify="center",
            wraplength=600
        ).grid(row=3, column=0, pady=(20, 10), sticky="n")

        # Texto para procurar um profissional
        ctk.CTkLabel(
            self.container,
            text=texto_procurar_profissiona,
            font=ctk.CTkFont(size=18, family='helvetica'),
            text_color="#696a76",
            justify="center",
            wraplength=600
        ).grid(row=6, column=0, sticky="s")

        # Botão para voltar
        ctk.CTkButton(
            self.container,
            text="Voltar ao menu inicial",
            width=600,
            height=40,
            command=self.retornar_a_home  # Sem parênteses!
        ).grid(row=7, sticky="s", pady=(10, 30))
    
    def atualizar(self):
        # Remove widgets antigos (opcional, se for recriar tudo)
        for widget in self.container.winfo_children():
            widget.destroy()
        self.carregar_resultado()

    def retornar_a_home(self):
        daltonismo.DaltonismoView.apagar_resultado(self)
        print("Daltonismo depois de apagar:", daltonismo.resultado)

        exame_ponto2.ExamePontoView2.apagar_resultado(self)
        print("Exame_Ponto depois de apagar:", exame_ponto2.resultado)

        astigmatismo2.AstigmatismoView2.apagar_resultado(self)
        print("Astigmatismo depois de apagar:", astigmatismo2.resultado)

        acuidade2.AcuidadeView2.apagar_resultado(self)
        print("Acuidade depois de apagar:", acuidade2.resultado)

        global resultado
        resultado = {}

        if self.controller:
            self.controller.switch("home")


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Resultado")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    class DummyController:
        def switch(self, view_name):
            print(f"Switching to: {view_name}")

    app = ResultadoView(root, controller=DummyController())
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
