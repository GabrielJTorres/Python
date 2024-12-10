# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os



def listar(todo):
    print()
    if not todo:
        print('Nenhuma tarefa pra listar')
        return
    print('Tarefas:')
    for tarefa in todo:
        print(f'\t{tarefa}')


def desfazer(todo, todo_redo):
    print()
    if not todo:
        print('Nenhuma tarefa pra desfazer')
        return
    todo = todo.pop()
    todo_redo.append(todo)

def refazer(todo, todo_redo):
    print()
    if not todo_redo:
        print('Nenhuma tarefa pra refazer')
        print()
        return
    todo = todo_redo.pop()
    todo_redo.append(todo)

def adicionar(tarefa, todo):
    print()
    tarefa = tarefa.strip( )
    if not tarefa:
        print('Você não digitou nada')
        return
    print(f'{tarefa=} adicionado à lista de tarefas')
    todo.append(tarefa)
    print()

todo = []
todo_redo = []

while True:
    print('Insira um item para adicionar na lista ou use os comandos seguintes: listar, clear, desfazer e refazer.')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(todo)
        continue

    elif tarefa == 'desfazer':
        desfazer(todo, todo_redo)
        listar(todo)
        continue

    elif tarefa == 'refazer':
        refazer(todo, todo_redo)
        listar(todo)
        continue

    elif tarefa == 'clear':
        os.system('cls')
        continue

    else:
        adicionar(tarefa, todo)
        listar(todo)
        print()
        continue