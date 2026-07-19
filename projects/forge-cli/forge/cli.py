import typer
from rich.console import Console

from forge.commands.doctor import doctor
from forge.commands.project import app as project_app

app = typer.Typer(
    name="forge",
    help="Forge - Your personal engineering system."
)

console = Console()

VERSION = "0.1.0"


@app.command()
def version():
    """Show Forge version."""
    console.print(f"🔥 Forge CLI v{VERSION}")


@app.command()
def info():
    """Show information about Forge."""
    console.print("🔥 Forge")
    console.print("Your personal engineering system.")
    console.print(f"Version: {VERSION}")


app.command()(doctor)

app.add_typer(
    project_app,
    name="project",
    help="Manage Forge projects."
)


if __name__ == "__main__":
    app()