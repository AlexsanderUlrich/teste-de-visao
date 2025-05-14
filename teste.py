import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Amostras de Fontes")
root.geometry("800x700")
root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
root.grid_columnconfigure(0, weight=1)

fontes_exemplo = [
    "Arial",
    "Helvetica",
    "Times New Roman",
    "Courier New",
    "Comic Sans MS",
    "Georgia",
    "Verdana",
    "Tahoma",
    "Calibri",
    "Consolas"
]

texto_amostra = "Exemplo de texto com a fonte:"

for i, fonte in enumerate(fontes_exemplo):
    try:
        label = ctk.CTkLabel(
            root,
            text=f"{texto_amostra} {fonte}",
            font=ctk.CTkFont(family=fonte, size=24),
            text_color="black"
        )
        label.grid(row=i, column=0, pady=5, padx=20, sticky="w")
    except Exception as e:
        print(f"Erro ao usar a fonte {fonte}: {e}")

root.mainloop()
