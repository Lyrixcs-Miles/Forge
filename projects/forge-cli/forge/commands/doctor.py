import subprocess
from rich.console import Console

console = Console()


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


def doctor():
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
