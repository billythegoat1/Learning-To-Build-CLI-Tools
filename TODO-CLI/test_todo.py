# We have 3 commands:
# - Create
# - List
# - Delete

#First create a dictionary containing priorities

# For Create, we need two options, the filepath of the file we are adding the task to, and the priority
# Default file path: mytodos_test
# Default priority: medium

import click
import json

@click.group
def mycommands():
    pass

PRIORITIES = {
    "l": "low",
    "m": "medium",
    "h": "high"
}

#Create Command
@click.command()

@click.option("-n", "--name",
                prompt="Enter the name of the todo")

@click.option("-d", "--desc",
                prompt="Enter the description")

@click.option("-f", "--filename",
              type=click.Path(exists=False),
              help="Name of the file",
              default="TODOS1.json",
              show_default=True)
@click.option("-p", "--priority",
              type=click.Choice(PRIORITIES.keys()),
              help="Enter the priority of the task",
              default="m",
              show_default=True)


def add (name, desc, priority, filename):
    new_task = {
        "name": name,
        "Description": desc,
        "Priority": PRIORITIES[priority],
    }
    #Load the tasks
    try:
        with open(filename, "r") as f:
           tasks = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    #Append the new task to the the list of tasks
    tasks.append(new_task)
    
    #Write the new list of tasks to the json file
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)
        
    click.echo("Task added successfully.")
    
#List Command
@click.command()

@click.option("-f",
              "--file",
              type = click.Path(exists=False),
              default="TODOS1.json",
              show_default=True)
@click.option("-p",
              "--priority",
              type = click.Choice(PRIORITIES.keys()),
              help="Enter the priority of the tasks",
              default=None,
              show_default=True)


def list(file, priority):
    try:
        with open(file, "r") as f:
            tasks = json.load(f)
            if not tasks:
                click.echo("😒, NO TASKS FOR TODAY!")
                return
            else:
                click.echo("\n📌 Your TODO List: \n")
                for idx, task in enumerate(tasks, start=1):
                    if priority is None or PRIORITIES[priority] == task["Priority"]:

                        click.echo(f"{idx}.{task['name']}")
                        click.echo(f"\n   📝Description: {task['Description']}")
                        click.echo(f"\n   🚦Priority: {task['Priority']}")
                        click.echo(f"\n" + "."*100)
                        
                    
    except(FileNotFoundError, json.JSONDecodeError):
        click.echo(" 🫤 No file was found! Please create one.")
        

mycommands.add_command(add)
mycommands.add_command(list)


if __name__ == "__main__":
    
    mycommands()