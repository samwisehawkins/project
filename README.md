# Project

This is a simple python project template to help standardise structure, without become too complex.

## Tools

  * conda / anaconda
  * git + GitHub
  * pytest
  * sphinx + napoleon


# Instructions

1.  Clone the template repo:
    
    git clone https://github.com/samwisehawkins/project.git

2.  Change the name of the project and the conda python environment
    
        mv project myproject 
        vi myproject/environment.yml  --> change environment name to match
        

3.  Change the package name, exit python modules etc. Generally adapt the project to your needs.

4.  Edit `setup.py` to reflect name changes

5.  Remove git history and re-initialise
    
        cd myproject 
        rm -rf .git 
        git init
        

6.  Create a virtual environment with the same name as the project
    
        cd myproject 
        conda env create -f environment.yml 
        source activate myproject
        

7.  Install your package into new virtual environment, using develop so it is symbolically linked to source code
    
        python setup.py develop
        

8.  Run tests
    
        pytest
        

9.  Create documentation structure (use `/doc` subdirectory as target)
    
        sphinx-quickstart
        

10. Edit doc/index.rst to auto-include modules and members:
    
        vi doc/index.rst
        .. automodule:: package.module
           :members:
        

11. Build the docs
    
        cd doc
        make html
        

12. Package and publish (coming soon).
