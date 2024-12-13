# ДЗ: Работа с классами и методами классов


class ToDoList:

    def __init__(self):
        self.__tasks__ = []

    def add_task(self, task: str):
        if not len(task):
            print(f"\nИмя задачи не может быть пустым.")
            return
        self.__tasks__.append({"name": task, "status": False})
        print(
            f"\nЗадача \"{self.__tasks__[-1]['name']}\" успешно добавлена в список под номером {len(self.__tasks__)}!.")

    def complete_task(self, task: int):
        if not 0 <= task - 1 < len(self.__tasks__):
            print("\nЗадача не найдена. ")
            return
        self.__tasks__[task - 1]["status"] = True
        print(f"\nСтатус задачи \"{self.__tasks__[task - 1]['name']}\" успешно изменен на \"Выполнено\"")

    def remove_task(self, task: int):
        if not 0 <= task - 1 < len(self.__tasks__):
            print("\nЗадача не найдена. ")
            return
        task_name = self.__tasks__[task - 1]['name'] or ""
        try:
            del (self.__tasks__[task - 1])
            print(f"\nЗадача \"{task_name}\" успешно удалена из списка задач")
        except Exception as e:
            print(f"\nЧто-то пошло не так ... : {e}")

    def list_tasks(self):
        if not self.__tasks__:
            print(f"\nСписок задач пуст. ")
            return
        print(f'\nNo- {"Название задачи": <80} - Выполнено?\n')
        for i, task in enumerate(self.__tasks__):
            status = "✓" if task["status"] else "X"
            print(f'{i + 1}- {task["name"]:_<90} {status}')


def prompt():
    print(f"""\n{'ToDo List':=^50}
1. Добавить задачу
2. Вывести список задач на экран
3. Отметить задачу как выполненную
4. Удалить задачу из списка
5. Выход""")

    return input("Выберите действие: ")


def main():
    my_task_list = ToDoList()

    menu = {
        1: my_task_list.add_task,
        2: my_task_list.list_tasks,
        3: my_task_list.complete_task,
        4: my_task_list.remove_task
    }

    while True:
        try:
            action = int(prompt())

            match action:
                case 1:
                    task = str(input("\nВведите название задачи: "))
                    menu[action](task)
                case 2:
                    menu[action]()
                case 3:
                    while True:
                        try:
                            task = int(input("\nВведите номер задачи для выполнения: "))
                            menu[action](task)
                            break
                        except ValueError:
                            print("Ошибка, введите число: ")
                case 4:
                    while True:
                        try:
                            task = int(input("\nВведите номер задачи для удаления: "))
                            menu[action](task)
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
