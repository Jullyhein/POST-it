import os

def read_annotation(filename):
    try:
        with open(filename, 'r') as file:
            annotations = file.readlines()
            annotations = [annotations.rstrip()
                           for annotation in annotations]
            return annotations
    except FileNotFoundError:
        return []

def save_annotation(filename, annotations):
    with open(filename, 'w') as file:
        notes = [annotation+'\n'for annotation in annotations]
        file.writelines(notes)

def show_annotation(annotation):
    len_annotation = len(annotation) + 6
    print('-', *len_annotation)
    print('-'* 3, annotation)
    print('-', * len_annotation)
    print()

def show_all_annotations(annotations):
    print('\n' + 'Annotations'.center(30, '='))
    for annotation in annotations:
        show_annotation(annotation)

def clean_touch():
    os.system('cls' if os.name =='nt' else 'clear')

def execute():
    filename = "annotations.txt"
    annotations = read_annotation(filename)

    while True:
        clean_touch()
        print("TODO APP")
        print("====\n")
        print("1. Addicted note")
        print("2. See annotations")
        print("3. out\n")

        action = input("Insert your action: ")
        if action == '1':
            annotation = input("Annotation: ")
            annotations.append(annotation)
            show_all_annotations(annotations)

        elif action == '2':
            show_annotation(annotations)
        elif action == '3':
            save_annotation(filename, annotations)
            break
        else:
            print("Opção inválida. ", end='')
            print("Please, try again", end='')
        input("\nPress Enter to continuing")
    if __name__ == "__main__":
        execute()




