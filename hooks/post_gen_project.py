import os
import shutil
from pathlib import Path

REMOVE_PATHS = []
MOVE_PATHS = []

# Dsharp and kissat require Docker to run on Windows. If we're not using either, 
# then we don't need Docker at all and can remove it from the generated project.
if "{{ cookiecutter.include_model_counting_support }}" == "n" and "{{ cookiecutter.sat_solver }}" == "default":
    REMOVE_PATHS.append("Dockerfile")
# If we're using Docker, then all the required libraries will be installed in the Docker 
# container so we won't need to have the requirements.txt.
else:
    REMOVE_PATHS.append("requirements.txt")
if "{{ cookiecutter.include_bauhaus }}" == "n":
    REMOVE_PATHS += ["run.py", "test.py"]

if "{{ cookiecutter.include_documentation_templates }}" == "word":
    REMOVE_PATHS.append("documents/docs.tex")
elif "{{ cookiecutter.include_documentation_templates }}" == "latex":
    REMOVE_PATHS.append("documents/docs.docx")

    
path_to_remove: str
for path_to_remove in REMOVE_PATHS:
    path_to_remove = path_to_remove.strip()
    if path_to_remove and os.path.exists(path_to_remove):
        if os.path.isdir(path_to_remove):
            shutil.rmtree(path_to_remove)
        else:
            os.unlink(path_to_remove)