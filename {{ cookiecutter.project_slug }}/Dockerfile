# start from base
FROM ubuntu:20.04

# install system-wide deps for python
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg build-essential vim git

# copy our application code
RUN mkdir /PROJECT
WORKDIR /PROJECT

# install required elements
RUN pip3 install --upgrade pip{% if cookiecutter.include_propositional_logic_modelling_support == "y" %}
RUN pip3 install nnf
RUN pip3 install bauhaus{% endif %}{% if cookiecutter.include_static_type_checking_support == "mypy" %}
RUN pip3 install mypy{% elif cookiecutter.include_static_type_checking_support == "pytype" %}
RUN pip3 install pytype{% endif %}{% if cookiecutter.include_string_markup_support == "sty" %}
RUN pip3 install sty{% elif cookiecutter.include_string_markup_support == "chalky" %}
RUN pip3 install chalky{% endif %}{% if cookiecutter.include_linting_support == "pylint" %}
RUN pip3 install pylint{% elif cookiecutter.include_linting_support == "flake8" %}
RUN pip3 install flake8{% endif %}

# install dsharp to run in the container
RUN curl https://mulab.ai/cisc-204/dsharp -o /usr/local/bin/dsharp
RUN chmod u+x /usr/local/bin/dsharp

# default command to execute when container starts
CMD /bin/bash
