usage: createProjectDirectories.py [-h] -p PROJECT -vc VERSIONCONTROL
                               [-r REPOSITORY]

Creates a directory and subdirectories for a version controlled project.
Starts either a mercurial (hg) or a git repo.
Project structure roughly follows the suggestions from:
[A Quick Guide to Organizing Computational Biology Projects](http://dx.doi.org/10.1371/journal.pcbi.1000424)


Directory structure:
Project/
- .git/
- data/
- doc/
- scripts/
- results/

Notes:
By default it assumes that the repo will live online in bitbucket, and the user name is also set to "adomingues".  Use options -r and -u to change this.


optional arguments:

-h, --help            
                    show this help message and exit

-p PROJECT, --project PROJECT
                    Project name. The root of the directory structure

-vc VERSIONCONTROL, --versionControl VERSIONCONTROL
                    Options: hg or git. Starts version control with list
                    of ignored files included.

-r REPOSITORY, --repository REPOSITORY
                    Options: github or bitbucket. Adds an online repo to
                    the VCS definitions.
