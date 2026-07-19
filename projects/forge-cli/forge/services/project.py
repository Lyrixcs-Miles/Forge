from pathlib import Path


FORGE_ROOT = Path.home() / "Forge"
PROJECTS_DIR = FORGE_ROOT / "projects"


def create_project(name: str):
    project_path = PROJECTS_DIR / name

    if project_path.exists():
        return False, project_path

    project_path.mkdir(parents=True)

    (project_path / "README.md").write_text(f"# {name}\n")
    (project_path / ".gitignore").write_text("")
    (project_path / "LICENSE").write_text("")
    (project_path / "src").mkdir()

    return True, project_path
