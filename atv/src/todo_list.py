class Task:
    def __init__(self, nome, descricao):
        if not nome.strip():
            raise ValueError("O nome da tarefa não pode ser vazio")
        self.nome = nome
        self.descricao = descricao
        self.status = "em andamento"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, nome, descricao):
        task = Task(nome, descricao)
        self.tasks.append(task)
        return task

    def mark_task_completed(self, tarefa):
        if tarefa.status == "concluída":
            return "Tarefa já está concluída"
        tarefa.status = "concluída"
        return "Status alterado para concluída"

    def mark_task_in_progress(self, tarefa):
        if tarefa.status == "concluída":
            raise ValueError("Não é possível marcar uma tarefa concluída como em andamento")
        tarefa.status = "em andamento"

    def edit_task(self, tarefa, novo_nome, nova_descricao):
        if tarefa not in self.tasks:
            raise ValueError("Tarefa não encontrada")
        if not novo_nome.strip():
            raise ValueError("Nome da tarefa não pode ser vazio")
        tarefa.nome = novo_nome
        tarefa.descricao = nova_descricao

    def delete_task(self, tarefa):
        if tarefa not in self.tasks:
            raise ValueError("Tarefa não encontrada")
        self.tasks.remove(tarefa)
