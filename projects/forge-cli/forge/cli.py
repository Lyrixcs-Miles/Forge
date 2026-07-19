import subprocess
import typer
from rich.console import Console

app = typer.Typer(
    name="forge",
    help="Forge - Your personal engineering system."
)

console = Console()

VERSION = "0.1.0"


def check_command(command: str):
    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout.strip() or result.stderr.strip()

        return True, output.split("\n")[0]

    except Exception:
        return False, "Not installed"


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


@app.command()
def doctor():
    """
    Check system health.
    """

    console.print("\n🔥 Forge Doctor\n")

    tools = [
        "python3",
        "git",
        "node",
        "code"
    ]

    healthy = True

    for tool in tools:
        installed, version = check_command(tool)

        if installed:
            console.print(f"✓ {tool}: {version}")

        else:
            console.print(f"✗ {tool}: Missing")
            healthy = False

    console.print()

    if healthy:
        console.print("Status: Healthy ✅")
    else:
        console.print("Status: Needs attention ⚠️")


if __name__ == "__main__":
    app()
