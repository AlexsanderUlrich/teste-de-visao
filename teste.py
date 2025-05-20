import customtkinter as ctk
from PIL import Image, ImageTk
import math
import os

ctk.set_appearance_mode("light")

class AnelCircularApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Anel Circular - Acuidade Visual")
        self.geometry("600x600")

        # Parâmetros do círculo
        self.qtd_botoes = 8
        self.raio = 1
        self.centro_x = 300
        self.centro_y = 300

        # Direções em graus (usadas para nome dos arquivos)
        self.angulos = [i * (360 // self.qtd_botoes) for i in range(self.qtd_botoes)]

        # Caminho das imagens
        self.caminho_topo = "assets/acuidade/abertura.png"  # imagem do anel superior
        self.caminho_botoes = "assets/acuidade"  # pasta com os botões

        # Ângulo correto (deve bater com o nome da imagem correta)
        self.angulo_correto = 120

        # Carregar imagem do topo (superior)
        self.imagem_topo = ImageTk.PhotoImage(Image.open(self.caminho_topo).resize((60, 60)))

        # Criar canvas
        self.canvas = ctk.CTkCanvas(self, width=600, height=600, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack()

        # Exibir imagem do topo (ex: abertura para 120°)
        self.canvas.create_image(self.centro_x, 100, image=self.imagem_topo)

        # Criar botões circulares com imagens diferentes
        self.botoes = []
        for ang in self.angulos:
            ajuste = ang - 90 
            x = self.centro_x + self.raio * math.cos(math.radians(ajuste))
            y = self.centro_y + self.raio * math.sin(math.radians(ajuste))

            # Nome do arquivo da imagem correspondente
            caminho_imagem = os.path.join(self.caminho_botoes, f"botao_{ang}.png")

            if not os.path.exists(caminho_imagem):
                print(f"Imagem não encontrada: {caminho_imagem}")
                continue

            imagem_botao = ImageTk.PhotoImage(Image.open(caminho_imagem).resize((300, 300)))
            
            img_id = self.canvas.create_image(x, y, image=imagem_botao)
            self.canvas.tag_bind(img_id, "<Button-1>", lambda e, a=ang: self.verificar_resposta(a))
            # salvar referência da imagem para evitar garbage collection
            self.botoes.append(imagem_botao)


        # Feedback
        self.feedback = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.feedback.pack(pady=10)

    def verificar_resposta(self, angulo_usuario):
        if angulo_usuario == self.angulo_correto:
            self.feedback.configure(text="✅ Correto!", text_color="green")
        else:
            self.feedback.configure(text="❌ Errado!", text_color="red")

if __name__ == "__main__":
    app = AnelCircularApp()
    app.mainloop()
