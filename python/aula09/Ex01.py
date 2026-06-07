import customtkinter as ctk  # Importa a biblioteca customtkinter

janela = ctk.CTk()  # Cria uma janela usando a biblioteca customtkinter
janela.title("Minha Janela")  # Define o título da janela
janela.geometry("600x400")  # Define o tamanho da janela
janela.configure(bg="#f0f0f0")  # Define a cor de fundo da janela
#janela.resizable(False, False)  # Impede que a janela seja redimensionada

janela.mainloop()  # Inicia o loop principal da janela