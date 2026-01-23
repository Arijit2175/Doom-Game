import os
import sys


def resource_path(relative_path: str) -> str:
    """Resolve resource paths for dev and PyInstaller bundles."""
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
