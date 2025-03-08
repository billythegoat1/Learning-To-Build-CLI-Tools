import click

@click.group
def mycommands():
    pass



PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}


@click.command()
#The priority of the task. THIS MUST BE PROVIDED. IF NOT, IT WILL BE SET TO MEDIUM(M)
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
#THE PATH TO THE FILE IS NOT REQUIRED(required=0)
@click.argument("todofile", type=click.Path(exists=False), default="mytodos.txt", required=False)
#The user is prompted to enter the name of the task
@click.option("-n", "--name", prompt="Enter the todo name", help="The name of the todo task")
#The user is prompted to enter a description for the task
@click.option("-d", "--description", prompt="Describe the todo task", help="The description of the todo task")
#Function to add a task
def add_task(name, description, priority, todofile):
    
    #a+ : Append to the file. If it doesn't exist we create it.
    with open(todofile, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]\n")
        

#Display the tasks
@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()), required=0)
@click.argument("todofile", type=click.Path(exists=True), default="mytodos.txt", required=0)
def list_task(priority, todofile):
    with open(todofile, "r") as f:
        
        todo_list = f.read().splitlines()
        if priority is None:
            for idx, task in enumerate(todo_list, start=1):
                print(f"({idx}) - {task}")
        else:
            for idx, task in enumerate(todo_list, start=1):
                if f"[Priority = {PRIORITIES[priority]}]" in task:
                    print(f"{idx} - {task}")
                        
#DELETE A TASK
@click.command() 
@click.argument("idx", type=int, required=True)
#Function to delete a todo task
def delete_task(idx):
    #r: reading mode
    with open("mytodos.txt", "r") as f:
        #We want sepatate each task on a single line
        todo_list = f.read().splitlines()
        #Then delete the one we want to delete
        todo_list.pop(idx-1)
        
        #Rewrite the remaining tasks in the file
    with open("mytodos.txt", "w") as f: 
        f.write("\n".join(todo_list))
        f.write('\n')

mycommands.add_command(add_task)
mycommands.add_command(list_task)
mycommands.add_command(delete_task)

if __name__ == "__main__":
    
    mycommands()
                    
    
