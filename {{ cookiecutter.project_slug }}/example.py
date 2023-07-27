{% if cookiecutter.include_bauhaus == "y" %}import nnf
import bauhaus
{% endif %}{% if cookiecutter.include_static_type_checking_support == "mypy" %}import mypy
{% elif cookiecutter.include_static_type_checking_support == "pytype" %}import pytype
{% endif %}{% if cookiecutter.include_string_markup_support == "sty" %}import sty
{% elif cookiecutter.include_string_markup_support == "chalky" %}import chalky
{% endif %}{% if cookiecutter.include_linting_support == "pylint" %}import pylint
{% elif cookiecutter.include_linting_support == "flake8" %}import flake8
{% endif %}

if __name__ == "__main__":
    pass