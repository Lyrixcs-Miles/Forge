import typer
from rich.console import Console

from forge.commands.doctor import doctor

app = typer.Typer(
    name="forge",
    help="Forge - Your personal engineering system."
)

console = Console()

VERSION = "0.1.0"


@app.command()
def version():
    console.print(f"🔥 Forge CLI v{VERSION}")


@app.command()
def info():
    console.print("🔥 Forge")
    console.print("Your personal engineering system.")
    console.print(f"Version: {VERSION}")


app.command()(doctor)


if __name__ == "__main__":
    app()
