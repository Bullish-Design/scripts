import subprocess
import argparse
import copier

from pathlib import Path

from scripts.config import SCRIPT_DIR


def main():
    parser = argparse.ArgumentParser(description="Create new uv script with name:")
    parser.add_argument("name", type=str, help="Name of script/library")
    args = parser.parse_args()

    script_name = args.name
    script_path = Path(SCRIPT_DIR) / script_name
    print(f"\n\nCreating new script '{script_name}' at location: {script_path}\n\n")
    script_path.mkdir(parents=True, exist_ok=True)
    creation_data = {
        "project_name": script_name,
        "project_description": f"{script_name.capitalize()} script.",
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
