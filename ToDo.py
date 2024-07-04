num = int(input("Введите сколько дел хотите сделать: "))

todo_list = []

for i in range(num):
    todo = input(f"Введите, что хотите сделать {i+1}: ")
    todo_list.append(todo)

with open("todo.txt", "w") as file:
    for i in range(0, len(todo_list), 2):
        file.write(todo_list[i])
        if i+1 < len(todo_list):
            file.write(" | " + todo_list[i+1] + "\n")
        else:
            file.write("\n")

print("Успешно сохранено в файл todo.txt")