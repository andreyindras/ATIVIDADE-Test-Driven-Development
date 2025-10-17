import unittest
from src.todo_list import ToDoList, Task

class ToDoListTestCase(unittest.TestCase):

    def test_adicionar_tarefa_com_nome_e_descricao(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar Python", "Revisar conceitos de TDD.")
        self.assertEqual(tarefa.nome, "Estudar Python")
        self.assertEqual(tarefa.descricao, "Revisar conceitos de TDD.")
        self.assertEqual(tarefa.status, "em andamento")

    def test_adicionar_tarefa_sem_nome_deve_levantar_erro(self):
        todo_list = ToDoList()
        with self.assertRaises(ValueError):
            todo_list.add_task("", "Descrição qualquer")

    def test_marcar_tarefa_como_concluida(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar", "Revisar conceitos")
        todo_list.mark_task_completed(tarefa)
        self.assertEqual(tarefa.status, "concluída")

    def test_tarefa_concluida_nao_pode_ser_marcada_novamente(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar", "Revisar conceitos")
        todo_list.mark_task_completed(tarefa)
        resultado = todo_list.mark_task_completed(tarefa)
        self.assertEqual(tarefa.status, "concluída")
        self.assertEqual(resultado, "Tarefa já está concluída")

    def test_marcar_tarefa_como_em_andamento(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar", "Revisar conceitos")
        todo_list.mark_task_in_progress(tarefa)
        self.assertEqual(tarefa.status, "em andamento")

    def test_nao_pode_marcar_concluida_como_em_andamento(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar", "Revisar conceitos")
        todo_list.mark_task_completed(tarefa)
        with self.assertRaises(ValueError):
            todo_list.mark_task_in_progress(tarefa)

    def test_editar_tarefa_existente(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar", "Revisar conceitos")
        todo_list.edit_task(tarefa, novo_nome="Estudar TDD", nova_descricao="Detalhes sobre TDD")
        self.assertEqual(tarefa.nome, "Estudar TDD")
        self.assertEqual(tarefa.descricao, "Detalhes sobre TDD")

    def test_editar_tarefa_inexistente_deve_levantar_erro(self):
        todo_list = ToDoList()
        tarefa_falsa = Task("Fake", "Fake desc")
        with self.assertRaises(ValueError):
            todo_list.edit_task(tarefa_falsa, novo_nome="Novo", nova_descricao="Novo")

    def test_excluir_tarefa_existente(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar", "Revisar conceitos")
        todo_list.delete_task(tarefa)
        self.assertNotIn(tarefa, todo_list.tasks)

    def test_excluir_tarefa_inexistente_deve_levantar_erro(self):
        todo_list = ToDoList()
        tarefa_falsa = Task("Fake", "Fake desc")
        with self.assertRaises(ValueError):
            todo_list.delete_task(tarefa_falsa)

if __name__ == '__main__':
    unittest.main()
