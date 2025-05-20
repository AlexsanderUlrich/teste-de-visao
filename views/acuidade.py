import customtkinter as ctk
from PIL import Image, ImageTk, ImageEnhance
import math
import os

# Cada item: (imagem_path, texto 1, texto 2, texto 3, número_correto, [opções])
teste = (
    "assets/acuidade/abertura.png",
     "1 - Tape o Olho Esquerdo.",
     "2 - Aproxime um pouco mais o seu dispositivo, deixando a distância de meio braço ou 30cm.",
     "3 - Foque no ponto negro no centro. Todas as linhas e quadrados parecem iguais e regulares?",
     0,
     [0, 45, 90, 135, 180, 225, 270, 315]
)
tamanhos = [4, 6, 8, 12, 18, 30, 46, 58]
angulos = [0, 45, 90, 135, 180, 225, 270, 315]
opcoes = {
    0: "assets/acuidade/botao_0.png",
    45: "assets/acuidade/botao_45.png",
    90: "assets/acuidade/botao_90.png",
    135: "assets/acuidade/botao_135.png",
    180: "assets/acuidade/botao_180.png",
    225: "assets/acuidade/botao_225.png",
    270: "assets/acuidade/botao_270.png",
    315: "assets/acuidade/botao_315.png"
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
Errar duas vezes o mesmo tamanho é vermelho.


"""

class AcuidadeView(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)        
        self.controller = controller
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        # Configura linhas e colunas para centralizar tudo
        self.grid_rowconfigure(0, weight=1)  # Espaço acima
        self.grid_rowconfigure(1, weight=0)  # container        
        self.grid_columnconfigure(0, weight=1)
        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)

        self.index = 0
        self.teste = teste
        self.angulos = angulos
        self.carregar_proximo()

    def carregar_proximo(self):
        print("Index do olho direito: ", self.index)
        if self.index >= 1:
            print("Resultado o exame ponto no olho direito: ", resultado)
            self.index = 0
            self.controller.switch("instrucoesExamePonto2")
            self.renderizar_novamente()
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        imagem_path, um, dois, tres, resposta_certa, opcoes = self.teste
        img = Image.open(imagem_path).resize((60, 60))
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
        centro_x, centro_y = 189, 133
        raio = 100
        angulos = self.angulos
        caminho_topo = "assets/acuidade/abertura.png"  # imagem do anel superior
        caminho_botoes = "assets/acuidade"  # pasta com os botões
        angulo_correto = 120

        imagem_topo = ImageTk.PhotoImage(Image.open(caminho_topo).resize((10, 10)))

        canvas = ctk.CTkCanvas(self.container, bg="white", highlightthickness=0)
        canvas.grid(row=5, column=0)

        canvas.create_image(centro_x, 60, image=imagem_topo)

        self.botoes = []
        self.imagens_hover = {}  # dicionário para armazenar versões com opacidade reduzida

        for ang in angulos:
            ajuste = ang - 90 
            x = centro_x + raio * math.cos(math.radians(ajuste))
            y = centro_y + raio * math.sin(math.radians(ajuste))

            caminho_imagem = os.path.join(caminho_botoes, f"botao_{ang}.png")

            if not os.path.exists(caminho_imagem):
                print(f"Imagem não encontrada: {caminho_imagem}")
                continue

            img_original = Image.open(caminho_imagem).convert("RGBA").resize((80, 80))
            imagem_botao = ImageTk.PhotoImage(img_original)

            # Criar imagem com opacidade reduzida (por exemplo, 50%)
            img_hover = img_original.convert("RGBA")
            alpha = img_hover.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.5)  # 50% opacity
            img_hover.putalpha(alpha)
            imagem_hover = ImageTk.PhotoImage(img_hover)

            img_id = canvas.create_image(x, y, image=imagem_botao)

            # Guardar as imagens para evitar garbage collection
            self.botoes.append(imagem_botao)
            self.botoes.append(imagem_hover)

            # Salvar no dicionário para usar no bind
            self.imagens_hover[img_id] = (imagem_botao, imagem_hover)

            # Bind do clique
            canvas.tag_bind(img_id, "<Button-1>", lambda e, a=ang, c=self.teste[4]: self.verificar_resposta(a, c))

            # Bind para mouse entrar - troca imagem para a versão com opacidade reduzida
            def make_on_enter(img_id):
                def on_enter(event):
                    normal, hover = self.imagens_hover[img_id]
                    canvas.itemconfigure(img_id, image=hover)
                return on_enter

            def make_on_leave(img_id):
                def on_leave(event):
                    normal, hover = self.imagens_hover[img_id]
                    canvas.itemconfigure(img_id, image=normal)
                return on_leave

            canvas.tag_bind(img_id, "<Enter>", make_on_enter(img_id))
            canvas.tag_bind(img_id, "<Leave>", make_on_leave(img_id))



    
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
