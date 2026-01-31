from pathlib import Path


def get_version_from_file() -> str:
    file_path = Path("VERSION")
    try:
        return f"v{file_path.read_text(encoding='utf - 8')}"
    except FileNotFoundError:
        print("File not found")
