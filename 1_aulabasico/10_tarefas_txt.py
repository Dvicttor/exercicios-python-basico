while True:
    print("\n1-Adicionar  2-Listar  3-Sair")
    op = input("Escolha: ")

    if op == "1":
        tarefa = input("Digite a tarefa: ")
        with open("tarefas.txt", "a") as f:
            f.write(tarefa + "\n")

    elif op == "2":
        try:
            with open("tarefas.txt", "r") as f:
                tarefas = f.readlines()
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t.strip()}")
        except FileNotFoundError:
            print("Nenhuma tarefa encontrada.")

    elif op == "3":
        break