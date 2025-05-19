import customtkinter as ctk
from PIL import Image, ImageTk

from . import astigmatismo


# Cada item: (imagem_path, texto 1, texto 2, texto 3, número_correto, [opções])
teste = (
    "assets/astigmatismo/astigmatismo_barras.png", 
     "1 - Tape o Olho Direito.",
     "2 - Aproxime um pouco mais o seu dispositivo, deixando a distância de meio braço ou 30cm.",
     "3 - Foque no centro do semicírculo. Todas as linhas aparecem na mesma tonalidade de preto?", 
     "Sim", 
     ["Sim", "Não"]
     )

# Adicionar aqui, o que vai ser exibido na tela de resultado.
resultado_direito = 0
resultado = {}

class AstigmatismoView2(ctk.CTkFrame):
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
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_rowconfigure(4, weight=1)
        self.container.grid_rowconfigure(5, weight=1)
        self.container.grid_rowconfigure(6, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.index = 0
        self.acertos = 0
        self.teste = teste
        self.carregar_proximo()

    def carregar_proximo(self):
        if self.index == 1:
            print("Resultado o exame ponto no olho direito: ", resultado)
            self.definir_resultado()
            self.index = 0
            self.reset()
            self.controller.switch("resultado")
            return

        for widget in self.container.winfo_children():
            widget.destroy()

        imagem_path, um, dois, tres, resposta_certa, opcoes = self.teste
        img = Image.open(imagem_path).resize((150, 75))
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

    def verificar_resposta(self, escolha, correta):
        if escolha == correta:
            self.acertos += 1     

        for btn in self.botoes:
            btn.configure(state="disabled")   

        self.after(1000, self.avancar)

    def definir_cor_olhos(self):
        global resultado
        global resultado_direito

        resultado_direito = astigmatismo.resultado

        if self.acertos > 0 and resultado_direito > 0:
            resultado["olho_direito"] = "azul"
            resultado["olho_esquerdo"] = "azul"
        elif self.acertos > 0 and resultado_direito == 0:
            resultado["olho_direito"] = "azul"
            resultado["olho_esquerdo"] = "vermelho"
        elif self.acertos == 0 and resultado_direito == 1:
            resultado["olho_direito"] = "vermelho"
            resultado["olho_esquerdo"] = "azul"
        else:
            resultado["olho_direito"] = "vermelho"
            resultado["olho_esquerdo"] = "vermelho"

    def definir_mensagem_final(self):
        global resultado
        resultado["titulo"] = "Astigmatismo"

        if resultado["olho_esquerdo"] == "vermelho" and resultado["olho_direito"] == "vermelho":
            resultado["mensagem"] = "Aparentemente, está a notar diferenças entre as linhas com ambos os olhos."
        elif resultado["olho_esquerdo"] == "azul" and resultado["olho_direito"] == "azul":
            resultado["mensagem"] = "Não aparenta ter sintomas de astigmatismo."
        else:
            resultado["mensagem"] = "Aparentemente, está a notar diferenças entre as linhas com um dos olhos."
        print("Mensagem dentro da view de astigmatismo2",resultado["mensagem"])
        
    def definir_resultado(self):     
        print("Exame de Astigmatismo, acertos OD", resultado_direito)
        print("Exame de Astigmatismo, acertos OE", self.acertos)

        self.definir_cor_olhos()
        self.definir_mensagem_final()

        print("Resultado final do exame de Astigmatismo: ", resultado)

    def avancar(self):
        self.index += 1
        self.carregar_proximo()

    def reset(self):
        self.acertos = 0
        astigmatismo.AstigmatismoView.reset(self)
        self.carregar_proximo()
    
    def apagar_resultado(self):
        global resultado
        global resultado_direito
        resultado = {}
        resultado_direito = 0
    
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Teste de Visão - Astigmatismo")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = AstigmatismoView2(root)
    app.grid(sticky="nsew")

    root.after(100, lambda: root.state("zoomed"))
    root.mainloop()
