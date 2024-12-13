# ДЗ: Работа с классами и методами классов


class ToDoList:

    def __init__(self):
        self.__tasks__ = []

    def add_task(self, task):
        if task:
            self.__tasks__.append({"name": task, "status": False})
            print(
                f"\nЗадача \"{self.__tasks__[-1]['name']}\" успешно добавлена в список под номером {len(self.__tasks__)}!.")

    def complete_task(self, task: int):
        if not 0 <= task - 1 < len(self.__tasks__):
            print("\nЗадача не найдена. ")
            return
        self.__tasks__[task - 1]["status"] = True
        print(f"Статус задачи \"{self.__tasks__[task - 1]['name']}\" успешно изменен на \"Выполнено\"")

    def remove_task(self, task: int):
        if not 0 <= task - 1 < len(self.__tasks__):
            print("Задача не найдена. ")
            return
        task_name = self.__tasks__[task - 1]['name'] or ""
        try:
            del (self.__tasks__[task - 1])
        except:
            print("Что-то пошло не так ... >_<")
        finally:
            print(f"Задача \"{task_name}\" успешно удалена из списка задач")

    def list_tasks(self):
        if self.__tasks__:
            print(f'\nNo- {"Название задачи": <80} - Выполнено?\n')
            for i, task in enumerate(self.__tasks__):
                print(f'{i + 1}- {task["name"]:_<90} {"✓" if task["status"] else "X"}')


def menu():
    print(f"\n{'ToDo List':=^50}")
    print("1. Добавить задачу")
    print("2. Вывести список задач на экран")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу из списка")
    print("5. Выход")

    return int(input("Выберите действие: "))


def main():
    my_task_list = ToDoList()

    while True:
        action = menu()

        match action:
            case 1:
                task = input("\nВведите название задачи: ")
                my_task_list.add_task(task)
            case 2:
                my_task_list.list_tasks()
            case 3:
                while True:
                    try:
                        task = int(input("\nВведите номер задачи для выполнения: "))
                        my_task_list.complete_task(task)
                        break
                    except ValueError:
                        print("Ошибка, введите число: ")
            case 4:
                while True:
                    try:
                        task = int(input("\nВведите номер задачи для удаления: "))
                        my_task_list.remove_task(task)
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


if __name__ == '__main__':
    main()
