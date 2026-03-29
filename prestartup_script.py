"""Prestartup Script (Clean version)."""
import shutil
from pathlib import Path

def copy_assets():
    SCRIPT_DIR = Path(__file__).resolve().parent
    # Adjust COMFYUI_DIR as needed; usually two levels up from custom_nodes/folder/
    COMFYUI_DIR = SCRIPT_DIR.parent.parent
    
    src = SCRIPT_DIR / "assets"
    dst = COMFYUI_DIR / "input"
    
    if src.exists():
        dst.mkdir(parents=True, exist_ok=True)
        for item in src.iterdir():
            if item.is_file():
                shutil.copy2(item, dst / item.name)
            elif item.is_dir():
                shutil.copytree(item, dst / item.name, dirs_exist_ok=True)
        print(f"Copied assets from {src} to {dst}")

if __name__ == "__main__":
    copy_assets()
