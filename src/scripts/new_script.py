import subprocess
import argparse
import copier

from pathlib import Path

from scripts.config import SCRIPT_DIR


def get_template_file_names(dir: str | Path):
    path_dir = Path(dir)
    all_files = path_dir.rglob("*")
    name_list = [f.stem for f in all_files]
    return name_list


def check_name(name: str, avoid_names: list[str]):
    if name in avoid_names:
        raise ValueError(f"Name '{name}' already exists in the template directory.")
        return False
    return True


def format_name(name: str):
    return name.lower().strip().replace(" ", "_").replace("-", "_")


def main():
    parser = argparse.ArgumentParser(description="Create new uv script with name:")
    parser.add_argument("name", type=str, help="Name of script/library")
    args = parser.parse_args()
    avoid_names = get_template_file_names(SCRIPT_DIR)

    script_name = args.name
    if not check_name(script_name, avoid_names):
        print(
            f"Name '{script_name}' already exists in the scripts directory. Try a different name."
        )
        exit()

    script_root = Path(SCRIPT_DIR)
    formatted_name = format_name(script_name)
    script_path = script_root / formatted_name

    print(f"\n\nCreating new script '{formatted_name}' at location: {script_path}\n\n")
    script_path.mkdir(parents=True, exist_ok=True)
    creation_data = {
        "project_name": formatted_name,
        "project_description": f"{formatted_name.capitalize()} script.",
    }
    # """
    copier.run_copy(
        "gh:Bullish-Design/scripts",
        str(script_path),
        unsafe=True,
        data=creation_data,
        defaults=True,
    )

    """
    subprocess.run(
        [
            # "uvx",
            "copier",
            "copy",
            "--trust",
            "gh:Bullish-Design/scripts",
            str(script_path),
            # "--"
        ],
        check=True,
    )
    """


if __name__ == "__main__":
    main()
