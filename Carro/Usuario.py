from Banco import Banco
from tkinter import messagebox

class Usuarios(object):
    def __init__(self, Usuario_id=0, Usu_nome="", User_name="", senha=""):
        self.info = {}
        self.Usuario_id = Usuario_id
        self.Usu_nome = Usu_nome
        self.User_name = User_name
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO Usuario (nome, user_name, senha) VALUES (?, ?, ?, ?, ?)",
                      (self.nome, self.user_name, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE Usuario SET nome = ?, user_name = ?, senha = ? WHERE Usuario_id = ?",
                      (self.nome, self.user_name, self.senha, self.Usuario_id))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM Usuario WHERE Usuario_id = ?", (self.Usuario_id,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"


    def selectAllUsers(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM Usuario")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            return f"Ocorreu um erro na recuperação dos usuários: {e}"
