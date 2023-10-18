# CustomTkinter Projects
Projetos usando CustomTkinter

## Installation
Install the module with pip:
```
pip3 install customtkinter
```
**Update existing installation:** ```pip3 install customtkinter --upgrade```\
(update as often as possible because this library is under active development)

## Documentation

The **official** documentation can be found here:

**➡️ https://customtkinter.tomschimansky.com/documentation**.

## Example Program
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

![image](https://github.com/Fabio-jr-SM/CustomTkinter-Projects/assets/91484736/bc5ecc21-1720-46c0-bc08-0a8453857746)

