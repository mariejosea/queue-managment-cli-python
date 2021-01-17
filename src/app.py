import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
#First in, first out
    
def print_queue():
    """ 
        This function: imprime en la consola la lista completa de la cola(queue),
        indicando la posición y el nombre del cliente.
    """
    print("Printing the entire list...")
    x = 0
    for i in queue.get_queue():
        name_in_list = queue.get_queue()[x]["name"]
        #last_name_in_list = queue.get_queue()[x]["last_name"]
        print(f"({x+1}) {name_in_list}")
        x+=1

def add():
    #se crean los input para preguntar al cliente
    #se crea un diccionario con los datos del cliente
    """
        This function: agrega un cliente a la cola, imprime que el cliente ha sido agregado,
        he imprime cuantas personas estan por delante del cliente utilizando la funcion enqueue
        que indica la longitud de la cola.
    """
    name = input("Enter client name: \n")
    phone_number = input("Enter phone number: \n")

    client = {
        "name": name,
        "phone_number": phone_number
    }

    print(f"\nHi {name}, you have ({queue.enqueue(client)}) people in front of you.")
    
def dequeue():
    """
        This function: guarda el primer elemento de la cola en una variable, imprime un mensaje en
        la consola indicando que el primer cliente será eliminado utilizando la función dequeue de
        la clase Queue. Y utilizando la función send() del archivo sms.py, se envia un mensaje al 
        cliente notificando su turno para comer.
    """
    name_ready_to_eat = queue.get_queue()[0]["name"]
    print(f"{name_ready_to_eat} was already called to eat and removed from the waiting list.")
    send("Hi " + name_ready_to_eat.upper() + ", your table is ready!!", queue.get_queue()[0]["phone_number"])
    queue.dequeue()

def save():
    # Writing JSON to a file in python
    def write_json(data, filename='queue.json'):
        #el archivo existe
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            #el archivo no existe
    with open('queue.json') as json_file:
        data = json.load(json_file)
    write_json(queue.get_queue())
    print("Saved queue!!")

def load():
    #Se debe importa json
    #Y abrir el archivo creado
    f = open('queue.json',)
    #Se devuleve un objeto json como dictionary
    data = json.load(f)
    queue.get_queue().clear()
    for index in data:
        queue.get_queue().append({"name":index["name"],"phone_number":index["phone_number"]})
    #Cerrar el archivo
    f.close()
    print("Loaded file in queue.json.")


print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        add()
        print("(Added client)")
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
