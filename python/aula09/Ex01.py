import customtkinter as ctk  # Importa a biblioteca customtkinter

janela = ctk.CTk()  # Cria uma janela usando a biblioteca customtkinter

janela.title("Minha Janela")  # Define o título da janela

janela.geometry("600x400")  # Define o tamanho da janela

janela.configure(bg="#6db43d")  # Define a cor de fundo da janela

#janela.resizable(False, False)  # Impede que a janela seja redimensionada



def criar_botao():
    print("Criando botão...")

def segundo_botao():
    print("Criando outro botão...")

botao_1 = ctk.CTkButton(janela, text="Entrar", command=criar_botao)  # Cria um botão usando a biblioteca customtkinter
botao_1.grid(row=0, column=0, padx=20, pady=20)  # Posiciona o botão na janela usando o gerenciador de layout grid

botao_2 = ctk.CTkButton(janela, text="Sair", command=segundo_botao)  # Cria outro botão usando a biblioteca customtkinter
botao_2.grid(row=1, column=1, padx=20, pady=20)  # Posiciona o segundo botão na janela usando o gerenciador de layout grid

botao_1._fg_color = "#ff0000"  # Altera a cor de fundo do primeiro botão para vermelho
botao_1._hover_color = "#66ff66"  # Altera a cor de fundo do primeiro botão quando o mouse estiver sobre ele para um tom mais claro de vermelho
botao_2._fg_color = "#00ff00"  # Altera a cor de fundo do segundo botão para verde
botao_2._hover_color = "#ff6666"  # Altera a cor de fundo do segundo botão quando o mouse estiver sobre ele para um tom mais claro de verde

janela.mainloop()  # Inicia o loop principal da janela