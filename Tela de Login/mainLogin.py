import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def Clique():
    print("Hello World")

texto = customtkinter.CTkLabel(janela, text="Fazer Login: ")
texto.pack(padx=10,pady=10)


email = customtkinter.CTkEntry(janela, placeholder_text="Seu Email")
email.pack(padx=10,pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10,pady=10)


checkBox = customtkinter.CTkCheckBox(janela,text="Salvar Login")
checkBox.pack(padx=10,pady=10)

botao = customtkinter.CTkButton(janela,text="Login",command=Clique)
botao.pack(padx=10,pady=10)



janela.mainloop()
