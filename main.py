import os
def load_todo_list():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
            return [task.strip() for task in f.readlines()]
    return []

def save_todo_list(todo_list):
    with open("todo.txt", "w") as f:
        for task in todo_list:
            f.write(task + "\n")

def show_todo_list(todo_list):
    print("Список дел:")
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)

def mark_task_done(todo_list, index):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1] += " [Выполнено]"

def edit_task(todo_list, index, new_task):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1] = new_task

def delete_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        del todo_list[index - 1]

def main():
    todo_list = load_todo_list()

    while True:
        show_todo_list(todo_list)
        print("Меню:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("0. Выйти")

        choice = int(input("Введите номер пункта меню: "))

        if choice == 1:
            task = input("Введите задачу: ")
            add_task(todo_list, task)
        elif choice == 2:
            index = int(input("Введите номер задачи для отметки: "))
            mark_task_done(todo_list, index)
        elif choice == 3:
            index = int(input("Введите номер задачи для редактирования: "))
            new_task = input("Введите новое содержание задачи: ")
            edit_task(todo_list, index, new_task)
        elif choice == 4:
            index = int(input("Введите номер задачи для удаления: "))
            delete_task(todo_list, index)
        elif choice == 0:
            save_todo_list(todo_list)
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
