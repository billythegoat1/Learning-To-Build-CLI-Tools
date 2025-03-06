import click

PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}

#The first command the user will enter
@click.command()

#The priority of the task. THIS MUST BE PROVIDED. IF NOT, IT WILL BE SET TO MEDIUM(M)
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")

#THE PATH TO THE FILE IS NOT REQUIRED(required=0)
@click.argument("todofile", type=click.Path(exists=False), required=0)

#The user can choose or not to provide the name of the todo task
@click.option("-n", "--name" prompt="Enter the todo name ", help="The name of the todo task")

#The user can choose or not to provid a description for the todo task
@click.option("-d", "--description", prompt="Describe the todo task", help="The description of the todo task")

#Function to add a task
def add_todo(name, description, priority, todofile):
    
    filename = todofile if todofile is not None else 'mytodos.txt'
    #a+ : Append to the file. If it doesn't exist we create it.
    with open(filename, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES}]")
        

@click.command() 
@click.argument("idx", type=int, required=1)
#Function to delete a todo task
def delete(idx):
    #r: reading mode
    with open("mytodos.txt", "r") as f:
        #We want to put the file in a variable before altering it
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
        
    with open("mytodos.txt", "w") as f: 
        f.write("\n".join(todo_list))
        f.write('\n')


if __name__ == "__main__":
    hello() 
    
