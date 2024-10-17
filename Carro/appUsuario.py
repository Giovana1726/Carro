from tkinter import *
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from Usuario import Usuarios

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")

        # Frame para o formulário
        self.janela1 = Frame(master)
        self.janela1.pack(padx=10, pady=10)

        # Título
        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        # Frame para a busca
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.Usuario_id_label = Label(self.janela2, text="Id usuário:")
        self.Usuario_id_label.pack(side="left")
        self.Usuario_id = Entry(self.janela2, width=20)
        self.Usuario_id.pack(side="left")

        self.busca = Button(self.janela2)
        self.busca["text"] = "Buscar"
        self.busca["command"] = self.buscarUsuario
        self.busca.pack()

        # Frames para os campos de dados
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.user_name_label = Label(self.janela5, text="User_name:")
        self.user_name_label.pack(side="left")
        self.user_name = Entry(self.janela5, width=28)
        self.user_name.pack(side="left")

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.senha_label = Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela4, width=30)
        self.senha["show"] = "*"
        self.senha.pack(side="left")

        # Frame para os botões
        self.janela10 = Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        self.botao4 = Button(self.janela11, width=10, text="Voltar", command=self.voltarParaMenu)
        self.botao4.pack(side="left")

        self.botao5 = Button(self.janela11, width=10, text="Exportar PDF", command=self.exportar_para_pdf)
        self.botao5.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "User_name"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("User_name", text="User_name")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def atualizarTabela(self):
        user = Usuarios()
        usuario = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuario:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4]))

    def buscarUsuario(self):
        user = Usuarios()
        Usuario_id = self.Usuario_id.get()
        self.autentic["text"] = user.selectUser(Usuario_id)
        self.idusuario.delete(0, END)
        self.idusuario.insert(INSERT, user.Usuario_id)
        self.nome.delete(0, END)
        self.nome.insert(INSERT, user.nome)
        self.user_name.delete(0, END)
        self.user_name.insert(INSERT, user.user_name)
        self.senha.delete(0, END)
        self.senha.insert(INSERT, user.senha)

        # Atualiza a tabela com o usuário encontrado
        self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.user_name = self.user_name.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.limparCampos()
        self.atualizarTabela()

    def alterarUsuario(self):
        user = Usuarios()
        user.Usuario_id = self.Usuario_id.get()
        user.nome = self.nome.get()
        user.user_name = self.user_name.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.updateUser()
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.Usuario_id = self.Usuario_id.get()
        self.autentic["text"] = user.deleteUser()
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.Usuario_id.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)
        self.tree.delete(*self.tree.get_children())

    def voltarParaMenu(self):
        self.master.destroy()  # Fecha a janela atual
        import Principal  # Recarrega o módulo Principal
        root = Tk()
        app = Principal.MainMenu(master=root)
        root.mainloop()

    def exportar_para_pdf(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()

        if isinstance(usuarios, str):
            messagebox.showerror("Erro", usuarios)
            return

        pdf_file = "relatorio_usuarios.pdf"

        try:
            with PdfPages(pdf_file) as pdf:
                fig, ax = plt.subplots(figsize=(12, 8))

                # Configuração do layout da tabela
                ax.set_axis_off()

                # Converte os dados para o formato necessário
                col_labels = ["ID", "Nome", "Telefone", "E-mail", "Usuário"]
                cell_text = [list(u) for u in usuarios]  # Transformando cada tupla em uma lista

                tbl = ax.table(
                    cellText=cell_text,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center',
                    bbox=[0, 0, 1, 1]  # Ajusta a tabela para preencher a figura
                )

                tbl.auto_set_font_size(False)
                tbl.set_fontsize(10)
                tbl.auto_set_column_width(range(len(col_labels)))
                tbl.scale(1.2, 1.2)

                ax.set_title("Relatório de Usuários", fontweight="bold", fontsize=16)

                pdf.savefig(fig)
                plt.close()

            messagebox.showinfo("Sucesso", f"PDF exportado com sucesso como '{pdf_file}'.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao exportar o PDF: {e}")
