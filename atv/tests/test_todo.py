import unittest
from src.todo_list import ToDoList

class ToDoListTestCase(unittest.TestCase):
    def test_adicionar_tarefa_com_nome_e_descricao(self):
        todo_list = ToDoList()
        tarefa = todo_list.add_task("Estudar Python", "Revisar conceitos de TDD.")
        self.assertEqual(tarefa.nome, "Estudar Python")
        self.assertEqual(tarefa.descricao, "Revisar conceitos de TDD.")
        self.assertEqual(tarefa.status, "em andamento")

if __name__ == '__main__':
    unittest.main()
