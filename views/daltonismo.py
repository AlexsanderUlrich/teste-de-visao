from tkinter import Frame, Label, Button
import tkinter as tk


class DaltonismoView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=0, sticky="nsew")  # Garantir que ocupe toda a tela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        container = tk.Frame(self, bg="white")
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)  # Espaço acima
        container.grid_rowconfigure(2, weight=1)  # Espaço abaixo
        
        content_frame = tk.Frame(container, bg="white")
        content_frame.grid(row=1, column=0)

            # Título
        tk.Label(
            content_frame,
            text="Teste de Visão\nRSData",
            font=("Roboto", 48, "bold"),
            fg="white",
            bg="#1c1c1c",
            justify="center"
        ).pack(pady=(0, 20))
