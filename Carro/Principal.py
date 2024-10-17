import tkinter as tk
from logging import root
from tkinter import messagebox
from appUsuario import Application as UserForm

class MainMenu:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Gestão")

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        self.title_label = tk.Label(self.frame, text="Menu Principal", font=("Verdana", 16, "bold"))
        self.title_label.pack(pady=10)

        # Botão para acessar a tela de usuários
        self.user_button = tk.Button(self.frame, text="Usuários", width=20, command=self.open_user_screen)
        self.user_button.pack(pady=5)

        # Botão para acessar a tela de cidades
        self.city_button = tk.Button(self.frame, text="Carros", width=20, command=self.open_city_screen)
        self.city_button.pack(pady=5)

        # Botão para acessar a tela de clientes
        self.client_button = tk.Button(self.frame, text="Clientes", width=20, command=self.open_client_screen)
        self.client_button.pack(pady=5)

        # Botão para sair do sistema
        self.exit_button = tk.Button(self.frame, text="Sair", width=20, command=self.master.quit)
        self.exit_button.pack(pady=5)

    def open_user_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = UserForm(self.new_window)



