import customtkinter as ctk
from PIL import Image, ImageTk, ImageEnhance
import math
import os
import random

# Cada item: (imagem_path, texto 1, texto 2, texto 3, número_correto, [opções])
teste = (
    "assets/acuidade/abertura.png",
    "1 - Tape o Olho Esquerdo.",
    "2 - Mantenha o dispositivo à distância de um braço",
    "3 - Consegue ver o anel superior? Marque a abertura correspondente no anel inferior.",
)

tamanhos = [4, 6, 8, 12, 18, 30, 46, 58]
angulos = [0, 45, 90, 135, 180, 225, 270, 315]
opcoes = {
    ang: f"assets/acuidade/botao_{ang}.png" for ang in angulos
}

pesos_tamanho = {
    4: 8,
    6: 7,
    8: 6,
    12: 5,
    18: 4,
    30: 3,
    46: 2,
    58: 1
}

resultado = 0


class AcuidadeView(ctk.CTkFrame):
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

        self.index = 0
        self.teste = teste
        self.angulos = angulos
        self.tamanhos = tamanhos
        self.tamanho_index = 4  # Começa no índice 4 -> tamanho 18
        self.erros_por_tamanho = {}  # Para controle posterior
        self.angulo_atual = 0
        self.carregar_proximo()

    def carregar_proximo(self):
        if self.tamanho_index < 0 or self.tamanho_index >= len(self.tamanhos):
            print("Teste finalizado.")
            print("Resultado final:", resultado)
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        imagem_path, um, dois, tres = self.teste
        self.angulo_atual = random.choice(self.angulos)
        tamanho_atual = self.tamanhos[self.tamanho_index]

        # Orientações
        ctk.CTkLabel(self.container, text="Acuidade Visual", font=ctk.CTkFont(size=20, family='helvetica', weight="bold"), wraplength=1500, text_color="black", justify="center").grid(row=0, column=0, pady=(30, 10), sticky="n")
        ctk.CTkLabel(self.container, text=um, font=ctk.CTkFont(size=28, family='helvetica'), wraplength=1500, text_color="gray", justify="center").grid(row=1, column=0, pady=(30, 10), sticky="n")
        ctk.CTkLabel(self.container, text=dois, font=ctk.CTkFont(size=28, family='helvetica'), wraplength=1500, text_color="gray", justify="center").grid(row=2, column=0, pady=(0, 10), sticky="n")
        ctk.CTkLabel(self.container, text=tres, font=ctk.CTkFont(size=28, family='helvetica', weight="bold"), wraplength=1500, text_color="gray", justify="center").grid(row=3, column=0, pady=(0, 0), sticky="n")

        # Imagem do arco rotacionado
        img = Image.open(imagem_path).resize((tamanho_atual * 1, tamanho_atual * 1))
        img = img.rotate(self.angulo_atual)
        photo = ImageTk.PhotoImage(img)

        self.label_img = ctk.CTkLabel(self.container, image=photo, text="")
        self.label_img.image = photo
        self.label_img.grid(row=4, column=0, pady=100, sticky="ew")

        botoes_frame = ctk.CTkFrame(self.container, fg_color="white")
        botoes_frame.grid(row=5, column=0, sticky="s")

        self.botoes = []
        self.criar_anel()

    def verificar_resposta(self, escolha):
        global resultado
        tamanho_atual = self.tamanhos[self.tamanho_index]

        if escolha == self.angulo_atual:
            print(f"Acertou! Tamanho: {tamanho_atual} | Angulo: {self.angulo_atual} | Escolha: {escolha}")
            resultado += pesos_tamanho[tamanho_atual]
            if self.tamanho_index > 0:
                self.tamanho_index -= 1  # Aumenta dificuldade
        else:
            print(f"Errou! Tamanho: {tamanho_atual} | Angulo: {self.angulo_atual} | Escolha: {escolha}")
            self.erros_por_tamanho[tamanho_atual] = self.erros_por_tamanho.get(tamanho_atual, 0) + 1
            if self.tamanho_index < len(self.tamanhos) - 1:
                self.tamanho_index += 1  # Reduz dificuldade

        self.after(1000, self.avancar)

    def avancar(self):
        self.index += 1
        self.carregar_proximo()

    def renderizar_novamente(self):
        self.carregar_proximo()

    def reset(self):
        global resultado
        resultado = 0
        self.tamanho_index = 4
        self.erros_por_tamanho = {}

    def criar_anel(self):
        centro_x, centro_y = 189, 133
        raio = 100
        angulos = self.angulos
        caminho_botoes = "assets/acuidade"

        canvas = ctk.CTkCanvas(self.container, bg="white", highlightthickness=0)
        canvas.grid(row=5, column=0)

        self.botoes = []
        self.imagens_hover = {}

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

            img_hover = img_original.copy()
            alpha = img_hover.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
            img_hover.putalpha(alpha)
            imagem_hover = ImageTk.PhotoImage(img_hover)

            img_id = canvas.create_image(x, y, image=imagem_botao)

            self.botoes.append(imagem_botao)
            self.botoes.append(imagem_hover)
            self.imagens_hover[img_id] = (imagem_botao, imagem_hover)

            canvas.tag_bind(img_id, "<Button-1>", lambda e, a=ang: self.verificar_resposta(a))

            def make_on_enter(img_id):
                def on_enter(event):
                    _, hover = self.imagens_hover[img_id]
                    canvas.itemconfigure(img_id, image=hover)
                return on_enter

            def make_on_leave(img_id):
                def on_leave(event):
                    normal, _ = self.imagens_hover[img_id]
                    canvas.itemconfigure(img_id, image=normal)
                return on_leave

            canvas.tag_bind(img_id, "<Enter>", make_on_enter(img_id))
            canvas.tag_bind(img_id, "<Leave>", make_on_leave(img_id))


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Acuidade Visual")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = AcuidadeView(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
