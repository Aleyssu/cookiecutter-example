import os
import shutil
from pathlib import Path

REMOVE_PATHS = []
MOVE_PATHS = []

# Dsharp, which is required for bauhaus (a propositional logic modelling python library), 
# requires Docker to run on Windows. If we're not using bauhaus, then we don't need Docker 
# at all and can remove it from the generated project.
if "{{ cookiecutter.include_propositional_logic_modelling_support }}" == "n":
    REMOVE_PATHS += ["Dockerfile", "run.py", "test.py"]
    
# If we're using Docker, then all the required libraries will be installed in the Docker 
# container so we won't need to have the requirements.txt.
else:
    REMOVE_PATHS.append("requirements.txt")

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