from cookiecutter.main import cookiecutter

# Create project from a local template
cookiecutter(
    # Specifies the file path to the template; 
    # in this case the python script is inside the template folder
    '.',  

    # Dictionary containing override values for the default values
    # in cookiecutter.json or .cookiecutterrc
    extra_context={
        'include_propositional_logic_modelling_support': 'y'
        'project_name': '{{ cookiecutter.course_code}} Modelling Project'
    },
    
    # Suppresses the command line prompts asking for input - this causes
    # only default values to be used for the variables (including override
    # values from extra_context).
    no_input=False,
    
    # Used for repos/main directories with multiple templates or templates 
    # within subdirectories from the root - specifies the path to the chosen 
    # template from the root directory.
    # Remember that the main directory can itself be the template directory,
    # where the directory argument would then not be needed.
    directory='.'
)

# Create project from the remote template
# cookiecutter('https://github.com/Aleyssu/cookiecutter-test')