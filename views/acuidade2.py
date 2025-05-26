import customtkinter as ctk
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import math
import os
import random

from . import acuidade

# Cada item: (imagem_path, texto 1, texto 2, texto 3)
teste = (
    "assets/acuidade/abertura.png",
    "1 - Tape o Olho direito.",
    "2 - Mantenha o dispositivo à distância de um braço",
    "3 - Consegue ver o anel superior? Marque a abertura correspondente no anel inferior.",
)
tamanhos = [6, 8, 10, 14, 20, 32, 48, 60]
pesos_tamanho = { 6: 8, 8: 7, 10: 6, 14: 5, 20: 4, 32: 3, 48: 2, 60: 1 }

angulos = [0, 45, 90, 135, 180, 225, 270, 315]
opcoes = { ang: f"assets/acuidade/botao_{ang}.png" for ang in angulos }
opcoes_verde = { ang: f"assets/acuidade/botao_{ang}_verde.png" for ang in angulos }
opcoes_vermelho = { ang: f"assets/acuidade/botao_{ang}_vermelho.png" for ang in angulos }

resultado_direito = 0
resultado_esquerdo = 0
resultado = {}

class AcuidadeView2(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)

        self.index = 0 # Index de quantos perguntas foram respondidas
        self.teste = teste 
        self.angulos = angulos
        self.tamanhos = tamanhos
        self.tamanho_index = 4  # Começa no índice 4 -> tamanho 18px
        self.angulo_atual = 0
        self.botoes_anel = {}
        self.carregar_proximo()

    def carregar_proximo(self):
        if self.index == 8:
            print("Resultado do exame de acuidade no olho esquerdo:", resultado_esquerdo)
            self.definir_resultado()
            self.reset()
            self.controller.switch("resultado")
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        self.feedback_id = None  # Para limpar depois
        imagem_path, um, dois, tres = self.teste
        self.angulo_atual = random.choice(self.angulos) # Adiciona aleatóriamente um dos ângulos a variavel.
        tamanho_atual = self.tamanhos[self.tamanho_index]

        # Orientações
        ctk.CTkLabel(self.container, text="Acuidade Visual", font=ctk.CTkFont(size=20, family='helvetica', weight="bold"), wraplength=1500, text_color="black", justify="center").grid(row=0, column=0, pady=(30, 10), sticky="n")
        ctk.CTkLabel(self.container, text=um, font=ctk.CTkFont(size=28, family='helvetica'), wraplength=1500, text_color="#696a76", justify="center").grid(row=1, column=0, pady=(30, 10), sticky="n")
        ctk.CTkLabel(self.container, text=dois, font=ctk.CTkFont(size=28, family='helvetica'), wraplength=1500, text_color="#696a76", justify="center").grid(row=2, column=0, pady=(0, 10), sticky="n")
        ctk.CTkLabel(self.container, text=tres, font=ctk.CTkFont(size=28, family='helvetica', weight="bold"), wraplength=1500, text_color="#696a76", justify="center").grid(row=3, column=0, pady=(0, 0), sticky="n")

        # Imagem do arco rotacionado.
        escala = 4
        tam = tamanho_atual * escala #estava perdendo resolução ao rotacionar, por isso primeiro aumenta a escala dela e depois reduz, mantendo a resolução da imagem.
        img = Image.open(imagem_path).convert("RGBA")
        img = img.resize((tam, tam), resample=Image.BICUBIC)
        img = img.rotate(self.angulo_atual, expand=True, resample=Image.BICUBIC) # Rotaciona a imagem
        img = ImageOps.mirror(img) # Por conta de trabalhar essa rotação diferente da disposição dos botões de resposta, tem que espelhar a imagem depois de rotacionar.
        img = img.resize((tamanho_atual, tamanho_atual), resample=Image.LANCZOS)

        photo = ImageTk.PhotoImage(img)

        self.label_img = ctk.CTkLabel(self.container, image=photo, text="", anchor="center")
        self.label_img.image = photo
        self.label_img.grid(row=4, column=0, pady=100, sticky="ew")

        botoes_frame = ctk.CTkFrame(self.container, fg_color="white")
        botoes_frame.grid(row=5, column=0, sticky="s")

        self.botoes = []
        self.imagens_hover = {}
        self.criar_anel()

    def verificar_resposta(self, escolha):
        global resultado_esquerdo
        tamanho_atual = self.tamanhos[self.tamanho_index]

        # Remover botão central anterior, se houver
        if hasattr(self, "feedback_id") and self.feedback_id is not None:
            self.canvas.delete(self.feedback_id)
            self.feedback_id = None

        # Alterar imagens dos botões para refletir acerto/erro
        # Primeiro, colore todos normais
        for ang, btn_id in self.botoes_anel.items():
            caminho_img = opcoes[ang]
            img_original = Image.open(caminho_img).convert("RGBA").resize((80, 80))
            imagem_botao = ImageTk.PhotoImage(img_original)
            self.imagens_hover[btn_id] = (imagem_botao, self.imagens_hover[btn_id][1])
            self.canvas.itemconfigure(btn_id, image=imagem_botao)
            # Atualiza referência para evitar garbage collection
            self.botoes.append(imagem_botao)

        if escolha == self.angulo_atual:
            print(f"Acertou! Tamanho: {tamanho_atual} | Angulo: {self.angulo_atual} | Escolha: {escolha}")
            resultado_esquerdo += pesos_tamanho[tamanho_atual]
            cor_feedback = "#00a170"
            simbolo = "✓"
            if self.tamanho_index > 0:
                self.tamanho_index -= 1

            # Botão escolhido fica verde
            caminho_verde = opcoes_verde[escolha]
            img_verde = Image.open(caminho_verde).convert("RGBA").resize((80, 80))
            foto_verde = ImageTk.PhotoImage(img_verde)
            btn_id = self.botoes_anel[escolha]
            self.canvas.itemconfigure(btn_id, image=foto_verde)
            self.imagens_hover[btn_id] = (foto_verde, self.imagens_hover[btn_id][1])
            self.botoes.append(foto_verde)

        else:
            print(f"Errou! Tamanho: {tamanho_atual} | Angulo: {self.angulo_atual} | Escolha: {escolha}")
            cor_feedback = "#ab0037"
            simbolo = "✗"
            if self.tamanho_index < len(self.tamanhos) - 1:
                self.tamanho_index += 1

            # Botão escolhido fica vermelho
            caminho_vermelho = opcoes_vermelho[escolha]
            img_vermelho = Image.open(caminho_vermelho).convert("RGBA").resize((80, 80))
            foto_vermelho = ImageTk.PhotoImage(img_vermelho)
            btn_id = self.botoes_anel[escolha]
            self.canvas.itemconfigure(btn_id, image=foto_vermelho)
            self.imagens_hover[btn_id] = (foto_vermelho, self.imagens_hover[btn_id][1])
            self.botoes.append(foto_vermelho)

            # Botão correto fica verde
            caminho_verde = opcoes_verde[self.angulo_atual]
            img_verde = Image.open(caminho_verde).convert("RGBA").resize((80, 80))
            foto_verde = ImageTk.PhotoImage(img_verde)
            btn_id = self.botoes_anel[self.angulo_atual]
            self.canvas.itemconfigure(btn_id, image=foto_verde)
            self.imagens_hover[btn_id] = (foto_verde, self.imagens_hover[btn_id][1])
            self.botoes.append(foto_verde)                

        # Adicionar botão com ✓ ou ✗ no centro do anel
        self.feedback_id = self.canvas.create_text(189, 133, text=simbolo, fill=cor_feedback, font=("Helvetica", 48, "bold"))
        # Vai para a próxima imagem depois de um delay de 1000 milisegundos.
        self.after(1000, self.avancar)

    def avancar(self):
        self.index += 1
        self.carregar_proximo()
    
    def definir_mensagem_final(self, resultado):
        if resultado["olho_esquerdo"] == "vermelho" and resultado["olho_direito"] == "vermelho":
            resultado["mensagem"] = "A sua acuidade visual em ambos os olhos parece ser reduzida."
        elif resultado["olho_esquerdo"] == "vermelho" or resultado["olho_direito"] == "vermelho":
            resultado["mensagem"] = "A sua acuidade visual em um dos olhos parece ser reduzida."
        elif resultado["olho_esquerdo"] =="azul" and resultado["olho_direito"] == "azul":
            resultado["mensagem"] = "A sua acuidade visual em ambos os olhos parece ser Excelente."
        else:
            resultado["mensagem"] = "A sua acuidade visual em ambos os olhos parece ser boa"

    def cor_olho_direito(self, resultado_final, resultado_direito):
        if resultado_direito <= 20:
            resultado_final["olho_direito"] = "vermelho"
        elif resultado_direito >= 36:
            resultado_final["olho_direito"] = "azul"
        else:
            resultado_final["olho_direito"] = "amarelo"

    def cor_olho_esquerdo(self, resultado_final, resultado_esquerdo):       
        if resultado_esquerdo <= 20:
            resultado_final["olho_esquerdo"] = "vermelho"
        elif resultado_esquerdo >= 36:
            resultado_final["olho_esquerdo"] = "azul"
        else:
            resultado_final["olho_esquerdo"] = "amarelo" 

    def definir_resultado(self):
        global resultado
        global resultado_esquerdo
        global resultado_direito
        resultado_direito = acuidade.resultado

        print("Exame de acuidade visual, média ponderada do OD: ", resultado_direito)
        print("Exame de acuidade visual, média ponderada do OE: ", resultado_esquerdo)       
              
        resultado["titulo"] = "Acuidade Visual"
        self.cor_olho_direito(resultado, resultado_direito)
        self.cor_olho_esquerdo(resultado, resultado_esquerdo)
        self.definir_mensagem_final(resultado)

        print("Resultado final do exame de acuidade visual: ", resultado)

    def reset(self):
        global resultado_esquerdo
        resultado_esquerdo = 0
        self.index = 0
        self.tamanho_index = 4
        self.carregar_proximo()
        acuidade.AcuidadeView.reset(self)
    
    def apagar_resultado(self):
        global resultado
        global resultado_direito
        global resultado_esquerdo

        resultado = {}
        resultado_direito = 0
        resultado_esquerdo = 0

    def criar_anel(self):
        centro_x, centro_y = 189, 133
        raio = 100
        angulos = self.angulos
        caminho_botoes = "assets/acuidade"

        self.canvas = ctk.CTkCanvas(self.container, bg="white", highlightthickness=0)
        self.canvas.grid(row=5, column=0)

        self.botoes = []
        self.imagens_hover = {}

        for ang in angulos:
            ajuste = ang - 90
            x = centro_x + raio * math.cos(math.radians(ajuste))
            y = centro_y + raio * math.sin(math.radians(ajuste))

            caminho_imagem = os.path.join(caminho_botoes, f"botao_{ang}.png")

            img_original = Image.open(caminho_imagem).convert("RGBA").resize((80, 80))
            imagem_botao = ImageTk.PhotoImage(img_original)

            img_hover = img_original.copy()
            alpha = img_hover.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
            img_hover.putalpha(alpha)
            imagem_hover = ImageTk.PhotoImage(img_hover)

            img_id = self.canvas.create_image(x, y, image=imagem_botao)


            self.botoes_anel[ang] = img_id
            self.botoes.append(imagem_botao)
            self.botoes.append(imagem_hover)
            self.imagens_hover[img_id] = (imagem_botao, imagem_hover)

            self.canvas.tag_bind(img_id, "<Button-1>", lambda e, a=ang: self.verificar_resposta(a))

            def make_on_enter(img_id):
                def on_enter(event):
                    _, hover = self.imagens_hover[img_id]
                    self.canvas.itemconfigure(img_id, image=hover)
                return on_enter

            def make_on_leave(img_id):
                def on_leave(event):
                    normal, _ = self.imagens_hover[img_id]
                    self.canvas.itemconfigure(img_id, image=normal)
                return on_leave

            self.canvas.tag_bind(img_id, "<Enter>", make_on_enter(img_id))
            self.canvas.tag_bind(img_id, "<Leave>", make_on_leave(img_id))


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Acuidade Visual")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = AcuidadeView2(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()