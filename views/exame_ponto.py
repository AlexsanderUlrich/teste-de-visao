import customtkinter as ctk
import random

from PIL import Image, ImageTk

# Cada item: (imagem_path, número_correto, [opções])
testes = [
    ("assets/exame_ponto/grade_olho.png", 
     "1 - Tape o Olho Esquerdo.",
     "2 - Aproxime um pouco mais o seu dispositivo, deixando a distância de meio braço ou 30cm.",
     "3 - Foque no ponto negro no centro. Todas as linhas e quadrados parecem iguais e regulares?", 
     "Sim", 
     ["Sim", "Não"]
     ),
    ("assets/exame_ponto/grade_olho.png", 
     "1 - Tape o Olho Esquerdo.",
     "2 - Aproxime um pouco mais o seu dispositivo, deixando a distância de meio braço ou 30cm.",
     "3 - Foque no ponto negro no centro. Alguma parte da grelha está em falta, distorcida ou mais escura do que as restantes?", 
     "Não", 
     ["Sim", "Não"]
     )
]

# Adicionar aqui, o que vai ser exibido na tela de resultado.
resultado =  {}

class ExamePontoView(ctk.CTkFrame):
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
        self.carregar_proximo()

    def carregar_proximo(self):
        if self.index >= len(self.testes):
            self.definir_resultado()
            self.reset()
            self.controller.switch("resultado")
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        imagem_path, um, dois, tres, resposta_certa, opcoes = self.testes[self.index]
        img = Image.open(imagem_path).resize((400, 400))
        photo = ImageTk.PhotoImage(img)

        # Orientações acima da imagem
        ctk.CTkLabel(
            self.container,
            text=um,
            font=ctk.CTkFont(size=28, family='helvetica'),
            text_color="gray",
            justify="center",
            wraplength=600
        ).grid(row=1, column=0, pady=(30, 10), sticky="n")

        ctk.CTkLabel(
            self.container,
            text=dois,
            font=ctk.CTkFont(size=28, family='helvetica'),
            text_color="gray",
            justify="center",
            wraplength=600
        ).grid(row=2, column=0, pady=(0, 10), sticky="n")

        ctk.CTkLabel(
            self.container,
            text=tres,
            font=ctk.CTkFont(size=28, family='helvetica', weight="bold"),
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
        if self.acertos == 6:
            resultado["titulo"] = "Visão cromática"
            resultado["mensagem"] = "A sua visão cromática parece ser Excelente."
            resultado["olho_esquerdo"] = "azul"
            resultado["olho_direito"] = "azul"
        elif self.acertos == 5:
            resultado["titulo"] = "Visão Cromática"
            resultado["mensagem"] = "A sua visão cromática parece ser boa"
            resultado["olho_esquerdo"] = "amarelo"
            resultado["olho_direito"] = "amarelo"
        else:
            resultado["titulo"] = "Visao Cromática"
            resultado["mensagem"] = "A sua visão cromática parece ser reduzida"
            resultado["olho_esquerdo"] = "vermelho"
            resultado["olho_direito"] = "vermelho"    
        print(resultado)

    def reset(self):
        self.index = 0
        self.acertos = 0
        self.testes = random.sample(testes, 6)
        self.carregar_proximo()
    


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Daltonismo")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = ExamePontoView(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
