from rich.console import Console
import typer

app = typer.Typer(
    name="forge",
    help="Forge - Your personal engineering system."
)

console = Console()

VERSION = "0.1.0"


@app.command()
def version():
    """
    Show Forge version.
    """
    console.print(f"🔥 Forge CLI v{VERSION}")


@app.command()
def info():
    """
    Show Forge information.
    """
    console.print("🔥 Forge")
    console.print("Your personal engineering system.")
    console.print(f"Version: {VERSION}")


if __name__ == "__main__":
    app()
