"""Execute the notebook in this Python environment; all science inputs are local."""
from pathlib import Path
import json
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

root = Path(__file__).resolve().parents[1]
path = root / "j1013_gaia_figures.ipynb"
notebook = nbformat.read(path, as_version=4)
nbformat.validate(notebook)
with tempfile.TemporaryDirectory(prefix="j1013-kernel-") as directory:
    spec_dir = Path(directory) / "j1013"
    spec_dir.mkdir()
    (spec_dir / "kernel.json").write_text(json.dumps({
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "J1013 active Python", "language": "python"}))
    manager = KernelManager(kernel_name="j1013", kernel_spec_manager=KernelSpecManager(kernel_dirs=[directory]),
                            transport="ipc",ip=str(Path(directory)/"kernel-ipc"),
                            connection_file=str(Path(directory)/"connection.json"))
    try:
        NotebookClient(notebook, km=manager, timeout=300,
                       resources={"metadata": {"path": str(root)}}).execute(cwd=str(root))
    finally:
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
nbformat.write(notebook, path)
print("All notebook cells executed successfully.")
