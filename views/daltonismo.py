import customtkinter as ctk
import random

from PIL import Image, ImageTk

# Cada item: (imagem_path, número_correto, [opções])
testes = [
    ("assets/visao_cromatica/0.png", "Nada", ["45", "5", "4", "Nada"]),
    ("assets/visao_cromatica/3.png", "3", ["84", "3", "2", "Nada"]),
    ("assets/visao_cromatica/5.png", "5", ["5", "7", "2", "Nada"]),
    ("assets/visao_cromatica/6.png", "6", ["45", "12", "6", "Nada"]),
    ("assets/visao_cromatica/8.png", "8", ["6", "8", "3", "Nada"]),
    ("assets/visao_cromatica/12.png", "12", ["45", "8", "12", "Nada"]),
    ("assets/visao_cromatica/29.png", "29", ["29", "8", "6", "Nada"]),
    ("assets/visao_cromatica/45.png", "45", ["5", "8", "45", "Nada"])
]

# Adicionar aqui, o que vai ser exibido na tela de resultado.
resultado =  {}

class DaltonismoView(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)        
        self.controller = controller
        self.configure(fg_color="white")
        self.grid(row=0, column=0, sticky="nsew")

        # Configura linhas e colunas para centralizar tudo
        self.grid_rowconfigure(0, weight=1)  # Espaço acima
        self.grid_rowconfigure(1, weight=1)  # container        
        self.grid_columnconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)

        self.index = 0
        self.acertos = 0
        self.testes = random.sample(testes, 6) # Pega aleatoriamente seis itens da lista de testes
        self.carregar_proximo()

    def carregar_proximo(self):
        if self.index >= len(self.testes):
            self.definir_resultado()
            self.reset()
            self.controller.switch("resultado")
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        imagem_path, resposta_certa, opcoes = self.testes[self.index]
        img = Image.open(imagem_path).resize((400, 400))
        photo = ImageTk.PhotoImage(img)

        # Nome do exame
        ctk.CTkLabel(
            self.container,
            text="Visão Cromática",
            font=ctk.CTkFont(size=20, family='helvetica', weight="bold"),
            wraplength=1500,
            text_color="black",
            justify="center"
        ).grid(row=0, column=0, pady=(30, 10), sticky="n")

        # Orientações acima da imagem
        ctk.CTkLabel(
            self.container,
            text="1 - Mantenha os dois olhos abertos.",
            font=ctk.CTkFont(size=28, family='helvetica'),
            text_color="gray",
            justify="center",
            wraplength=600
        ).grid(row=1, column=0, pady=(30, 10), sticky="n")

        ctk.CTkLabel(
            self.container,
            text="2 - Mantenha-se na marcação no chão.",
            font=ctk.CTkFont(size=28, family='helvetica'),
            text_color="gray",
            justify="center",
            wraplength=600
        ).grid(row=2, column=0, pady=(0, 10), sticky="n")

        ctk.CTkLabel(
            self.container,
            text="3 - Selecione o número que vê no circulo.",
            font=ctk.CTkFont(size=28, family='helvetica'),
            text_color="gray",
            justify="center",
            wraplength=600
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

    def verificar_resposta(self, escolha, correta):
        if escolha == correta:
            self.acertos += 1

        for btn in self.botoes:
            if btn.cget("text") == correta:
                btn.configure(fg_color="green", text=f"{correta} ✓")
            elif btn.cget("text") == escolha:
                btn.configure(fg_color="red", text=f"{escolha} ✗")
            btn.configure(state="disabled")

        self.after(1000, self.avancar)

    def avancar(self):
        self.index += 1
        self.carregar_proximo()

    def definir_resultado(self):
        global resultado
        resultado["titulo"] = "Visão cromática"
        if self.acertos == 6:
            resultado["mensagem"] = "A sua visão cromática parece ser excelente."
            resultado["olho_esquerdo"] = "azul"
            resultado["olho_direito"] = "azul"
        elif self.acertos == 5:
            resultado["mensagem"] = "A sua visão cromática parece ser boa"
            resultado["olho_esquerdo"] = "amarelo"
            resultado["olho_direito"] = "amarelo"
        else:
            resultado["mensagem"] = "A sua visão cromática parece ser reduzida"
            resultado["olho_esquerdo"] = "vermelho"
            resultado["olho_direito"] = "vermelho"    
        print(resultado)

    def reset(self):
        self.index = 0
        self.acertos = 0
        self.testes = random.sample(testes, 6)
        self.carregar_proximo()
    
    def apagar_resultado(self):       
        global resultado
        resultado = {}


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Daltonismo")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = DaltonismoView(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
