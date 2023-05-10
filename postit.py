import os 

notes = []
out = False

while not out:
    resp = input('Would U like to do annotation? (s/n)')
    if resp == 's':
        text = input("Annotation: ")
        notes.append(text)

    print('\n'+"Annotation".center(30, "="))

    #to layout about post-it
    for note in notes:
        text_size = len(note)
        note_size = text_size+6
        print('-'*note_size)
        print(note.center(note_size))
        print('-'*note_size)

    r = input("sair? (s/n)")
    if r == "s":
        sair = True
    os.system('cls' if os.name == 'nt' else 'clear')
