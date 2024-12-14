# ДЗ: Работа с классами и методами классов


class ToDoList:

    def __init__(self):
        self._tasks_ = []

    def add_task(self, task: str):
        if not len(task):
            print(f"\nИмя задачи не может быть пустым.")
            return
        self._tasks_.append({"name": task, "status": False})
        print(
            f"\nЗадача \"{self._tasks_[-1]['name']}\" успешно добавлена в список под номером {len(self._tasks_)}!.")

    def complete_task(self, task: int):
        if not 0 <= task - 1 < len(self._tasks_):
            print("\nЗадача не найдена. ")
            return
        self._tasks_[task - 1]["status"] = True
        print(f"\nСтатус задачи \"{self._tasks_[task - 1]['name']}\" успешно изменен на \"Выполнено\"")

    def remove_task(self, task: int):
        if not 0 <= task - 1 < len(self._tasks_):
            print("\nЗадача не найдена. ")
            return
        task_name = self._tasks_[task - 1]['name'] or ""
        try:
            del (self._tasks_[task - 1])
            print(f"\nЗадача \"{task_name}\" успешно удалена из списка задач")
        except Exception as e:
            print(f"\nЧто-то пошло не так ... : {e}")

    def list_tasks(self):
        if not self._tasks_:
            print(f"\nСписок задач пуст. ")
            return
        print(f'\nNo- {"Название задачи": <80} - Выполнено?\n')
        for i, task in enumerate(self._tasks_):
            status = "✓" if task["status"] else "X"
            print(f'{i + 1}- {task["name"]:_<90} {status}')


def main():
    my_task_list = ToDoList()

    menu = {
        1: (my_task_list.add_task, '1. Добавить задачу'),
        2: (my_task_list.list_tasks, '2. Вывести список задач на экран'),
        3: (my_task_list.complete_task, '3. Отметить задачу как выполненную'),
        4: (my_task_list.remove_task, '4. Удалить задачу из списка'),
    }

    while True:
        try:
            print(f"\n{'ToDo List':=^50}")
            for i in menu:
                print(menu[i][1])
            print(f"{len(menu) + 1}. Выход")

            action = int(input("Выберите действие: "))

            match action:
                case 1:
                    task = str(input("\nВведите название задачи: "))
                    menu[action][0](task)
                case 2:
                    menu[action][0]()
                case 3:
                    while True:
                        try:
                            task = int(input("\nВведите номер задачи для выполнения: "))
                            menu[action][0](task)
                            break
                        except ValueError:
                            print("Ошибка, введите число: ")
                case 4:
                    while True:
                        try:
                            task = int(input("\nВведите номер задачи для удаления: "))
                            menu[action][0](task)
                            break
                        except ValueError:
                            print("Ошибка, введите число: ")
                case 5:
                    print("\nСпасибо за пользование нашим списком задач. "
                          "\nВсе права не защищены."
                          "\nХорошего Вам дня.")
                    break
                case _:
                    print("Выберите пункт меню (1-5): ")
        except (ValueError, KeyError):
            print("Выберите пункт меню (1-5): ")


if __name__ == '__main__':
    main()
