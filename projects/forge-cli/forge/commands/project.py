import typer
from rich import print

from forge.services.project import create_project

app = typer.Typer()


@app.command()
def new(name: str):
    """Create a new project."""

    created, path = create_project(name)

    if created:
        print(f"[green]✓ Created[/green] {path}")
    else:
        print(f"[yellow]Project already exists:[/yellow] {path}")


@app.command("list")
def list_projects():
    """List projects."""
    print("[cyan]Coming soon...[/cyan]")