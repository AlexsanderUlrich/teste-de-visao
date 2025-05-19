import customtkinter as ctk
from PIL import Image, ImageTk
import math


# Cada item: (imagem_path, texto 1, texto 2, texto 3, número_correto, [opções])
teste = (
    "assets/acuidade/abertura.png",
     "1 - Tape o Olho Esquerdo.",
     "2 - Aproxime um pouco mais o seu dispositivo, deixando a distância de meio braço ou 30cm.",
     "3 - Foque no ponto negro no centro. Todas as linhas e quadrados parecem iguais e regulares?", 
     "Sim", 
     [0, 45, 90, 135, 180, 225, 270, 315]
)
tamanhos = [4, 6, 8, 12, 18, 30, 46, 58]
angulos = [0, 45, 90, 135, 180, 225, 270, 315]
opcoes = {
    0: "assets/acuidade/opcao_norte.png",
    45: "assets/acuidade/opcao_nordeste.png",
    90: "assets/acuidade/opcao_leste.png",
    135: "assets/acuidade/opcao_sudeste.png",
    180: "assets/acuidade/opcao_sul.png",
    225: "assets/acuidade/opcao_sudoeste.png",
    270: "assets/acuidade/opcao_oeste.png",
    315: "assets/acuidade/opcao_noroeste.png"
    }

quantidade_de_erros = {
    4: "", 
    6: "", 
    8: "", 
    12: 2, 
    18: "", 
    30: "", 
    46: "", 
    58: ""}

# Adicionar aqui, o que vai ser exibido na tela de resultado.
resultado = 0

"""
Errar dois é vermelho.


"""

class AcuidadeView(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)        
        self.controller = controller
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        # Configura linhas e colunas para centralizar tudo
        self.grid_rowconfigure(0, weight=1)  # Espaço acima
        self.grid_rowconfigure(1, weight=1)  # container        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)

        self.index = 0
        self.teste = teste
        self.carregar_proximo()

    def carregar_proximo(self):
        print("Index do olho direito: ", self.index)
        if self.index >= len(self.teste):
            print("Resultado o exame ponto no olho direito: ", resultado)
            self.index = 0
            self.controller.switch("instrucoesExamePonto2")
            self.renderizar_novamente()
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        imagem_path, um, dois, tres, resposta_certa, opcoes = self.teste
        img = Image.open(imagem_path).resize((250, 250))
        photo = ImageTk.PhotoImage(img)

        # Orientações acima da imagem
        ctk.CTkLabel(
            self.container,
            text=um,
            font=ctk.CTkFont(size=28, family='helvetica'),
            wraplength=1500,
            text_color="gray",
            justify="center"
        ).grid(row=1, column=0, pady=(30, 10), sticky="n")

        ctk.CTkLabel(
            self.container,
            text=dois,
            font=ctk.CTkFont(size=28, family='helvetica'),
            wraplength=1500,
            text_color="gray",
            justify="center"
        ).grid(row=2, column=0, pady=(0, 10), sticky="n")

        ctk.CTkLabel(
            self.container,
            text=tres,
            font=ctk.CTkFont(size=28, family='helvetica', weight="bold"),
            wraplength=1500,
            text_color="gray",
            justify="center"
        ).grid(row=3, column=0, pady=(0, 0), sticky="n")

        # Imagem 
        self.label_img = ctk.CTkLabel(self.container, image=photo, text="")
        self.label_img.image = photo
        self.label_img.grid(row=4, column=0, pady=100, sticky="ew")

        # Botões das respostas 
        botoes_frame = ctk.CTkFrame(self.container, fg_color="white")        
        botoes_frame.grid(row=5, column=0, sticky="s")

        self.botoes = []
        for i, opcao in enumerate(opcoes):
            btn = ctk.CTkButton(
                botoes_frame,
                text=opcao,
                width=80,
                height=40,
                command=lambda b=opcao: self.verificar_resposta(b, resposta_certa)
            )
            btn.grid(row=0, column=i, padx=10)
            self.botoes.append(btn)
        self.criar_anel()

    def verificar_resposta(self, escolha, correta):
        global resultado
        if escolha == correta:
            resultado += 1        

        self.after(1000, self.avancar)

    def avancar(self):
        self.index += 1
        self.carregar_proximo()
    
    def renderizar_novamente(self):
        self.carregar_proximo()

    def reset(self):
        global resultado
        resultado = 0        

    def criar_anel(self):
        centro_x, centro_y = 300, 300
        raio = 200
        tamanho_img = 50  # tamanho em pixels para a imagem no botão

        for angulo, caminho_img in opcoes.items():
            # Carregar imagem como CTkImage
            img = ctk.CTkImage(Image.open(caminho_img), size=(tamanho_img, tamanho_img))

            # Calcular posição baseada no ângulo
            rad = math.radians(angulo)
            x = centro_x + raio * math.cos(rad)
            y = centro_y - raio * math.sin(rad)  # y invertido porque eixo y cresce para baixo

            # Criar botão com imagem
            btn = ctk.CTkButton(
                self,
                image=img,
                text="",
                width=tamanho_img,
                height=tamanho_img,
                fg_color="transparent",
                hover=False,
                command=lambda angulo=angulo: self.selecionar(angulo)
            )
            btn.place(x=x - tamanho_img / 2, y=y - tamanho_img / 2)

    
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Campo de Visão")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = AcuidadeView(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
