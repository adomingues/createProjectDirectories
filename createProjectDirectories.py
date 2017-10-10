#!/usr/bin/python


from __future__ import (absolute_import, division,
                        print_function)
import argparse
import sys
import os
import shutil


usage = '''
   Creates a directory and subdirectories for a version controlled project.
   Starts either a mercurial (hg) or a git repo.
   Project structure follows roughly the suggestions from:
   A Quick Guide to Organizing Computational Biology Projects
   http://dx.doi.org/10.1371/journal.pcbi.1000424

   Directory structure:
   Project/
        .git/
        data/
        doc/
        scripts/
        results/

    Notes:
    By default it assumes that the repo will live online in bitbucket, and the user name is also set to "adomingues".  Use option -r to change this and/or edit directly in the code.
   '''


def getArgs():
    """Parse sys.argv"""
    parser = argparse.ArgumentParser(
        description=usage,
        formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument(
        '-p', '--project',
        required=True,
        type=str,
        help='Project name. The root of the directory structure'
    )
    parser.add_argument(
        '-vc', '--versionControl',
        required=True,
        type=str,
        help='Options: hg or git. Starts version control with list of ignored files included.'
    )
    parser.add_argument(
        '-r', '--repository',
        required=False,
        type=str,
        default="bitbucket",
        help='Options: github or bitbucket. Adds an online repo to thee VCS definitions.'
    )
    args = parser.parse_args()
    return args


def writeIgnore(fout):
    ignores = [
        'syntax: glob',
        '*.orig',
        '*.rej',
        '*~',
        '*.o',
        'tests/*.err',
        'data/*',
        'results/*',
        'Oler_raw_data/*',
        '*temp*',
        '*.rda',
        '*.RData',
        '*.gff',
        '*.gff3',
        '*.pdf',
        '*.PDF',
        '*.aux',
        '*.dvi',
        '*.log',
        '*.nav',
        '*.out',
        '*.snm',
        '*.toc',
        '*svg',
        '*Rhistory',
        '*DS_Store',
        '*.bed',
        '*.gtf',
        '*.loci',
        '*.stats',
        '*.tracking',
        '*.loci',
        '*.kate-swp',
        '*.svg',
        '*.xlsx',
        '<<<<<<< local',
        '=======',
        '*.xls',
        '*.backup',
        '*.gz',
        '*.rdb',
        '*.rdx',
        '*.bbl',
        '*.blg',
        '*.ods',
        '*.zip',
        ' ',
        '.bpipe/*',
        'commandlog.txt',
        '*.sublime-project',
        '*.sublime-workspace',
        '>>>>>>> other',
        ' ',
        'syntax: regexp',
        '.*\#.*\#$'
    ]

    with open(fout, 'w') as f:
        f.write('\n'.join(ignores))


def createFolders(project):
    folders = ['data', 'doc', 'scripts', 'results']

    if not os.path.exists(project):
        os.makedirs(project)
        os.chdir(project)

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    print("Template project directories are created.")


def startVC(project, vcs, repo):
    if vcs == "git":
        os.system("git init")
        ignore = '.gitignore'
    elif vcs == "hg":
        os.system("hg init")
        ignore = '.hgignore'
        if repo == 'bitbucket':
            repo_name = (
                "default = https://adomingues@bitbucket.org/adomingues/" +
                project)
            hgrc_file = open(".hg/hgrc", 'w')
            hgrc_file.write("[paths]\n")
            hgrc_file.write(repo_name+"\n")
            hgrc_file.close()
        else:
            pass
    writeIgnore(ignore)


def createDocs(project):
    print('Creating minimal docs for project')
    docs = ["doc/" + project + ".md",
            "README.md"
            ]
    for doc in docs:
        try:
            with open(doc, 'w'):
                pass
        except:
            print('Something went wrong! Could not create file')
            sys.exit(0)


def main():
    current_dir = os.getcwd()
    args = getArgs()
    project = args.project
    repo = args.repository
    print("The project's name is: ", project)
    if args.versionControl == "git":
        vcs = args.versionControl
    elif args.versionControl == "hg":
        vcs = args.versionControl
    else:
        print('No version control system provided.')

    createFolders(project)
    createDocs(project)
    startVC(project, vcs, repo)
    os.chdir(current_dir)


if __name__ == "__main__":
    main()
