from tkinter import *
import app_estructura

def main():
    root = Tk()
    root.title('Agenda de Contactos')
    root.configure(bg = "#FFFFFF")
    root.geometry("+350+80")
    root.resizable(0,0)
    app_estructura.App(root)
    root.mainloop()

if __name__ == "__main__":
    main()