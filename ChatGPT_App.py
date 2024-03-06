from openai import OpenAI
from rich import print
from rich.table import Table
import config
import os
import typer


def main():
    api_key = config.api_key
    os.environ["OPENAI_API_KEY"] = api_key
    client = OpenAI()
    messages = []

    print("[bold green]🗨️ ChatGPT App by Damian[/bold green]")

    table = Table("Command", "Description")
    table.add_row("exit", "Exit application")
    table.add_row("new", "New conversation")

    print(table)

    while True:
        prompt = __prompt()
        messages.append({"role": "user", "content": prompt})

        if prompt == "new":
            print("[bold magenta]👻 New conversation[/bold magenta]")
            messages = []
            prompt = __prompt()

        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo-0125", # GPT-3 Turbo
            #model="gpt-4-0125-preview" # GPT-4 Turbo
        )


        response_content = response.choices[0].message.content
        messages.append(response.choices[0].message)
        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\nChatGPT: Hi! What do you wanna talk?")

    if prompt == "exit":
        exit = typer.confirm("❗ Do you really want to exit?") #To put an emoji: "Windows/Command + ."
        if exit:
            print("[bold magenta]Goodbye![/bold magenta] 👋")
            raise typer.Abort()
        
        return __prompt()
    
    return prompt


if __name__ == "__main__":
    typer.run(main)