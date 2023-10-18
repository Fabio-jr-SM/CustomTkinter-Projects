# CustomTkinter Projects
Projetos usando CustomTkinter

## Instalação
instalação do modulo com pip:
```
pip3 install customtkinter
```
**Update existing installation:** ```pip3 install customtkinter --upgrade```\
(update as often as possible because this library is under active development)

## Documentação

The **official** documentation can be found here:

**➡️ https://customtkinter.tomschimansky.com/documentation**.

## Progama de Exemplo
To test customtkinter you can try this simple example with only a single button:
```python
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
```
![image](https://github.com/Fabio-jr-SM/CustomTkinter-Projects/assets/91484736/1bf39919-2bc4-437d-989c-99c65574ee34)


