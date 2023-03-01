import argparse
import pygit2
from pathlib import Path


def gen_parser():
    parser = argparse.ArgumentParser(
        prog='latextart',
        description='Start a new LaTeX project')

    parser.add_argument(
        'project_name',
        help='Name of the new project')

    parser.add_argument(
        '-l',
        '--language',
        action='store_const',
        const='es',
        default='en')

    return parser



def gen_project(project_name, language='en'):
    repo_url = 'https://github.com/Xein234/plantilla-tarea-latex'
    repo_dir = Path('plantilla-tarea-latex')
    es_branch = 'es'
    repo = pygit2.clone_repository(repo_url, str(repo_dir))
    if language == 'es':
        repo.checkout(repo.branches[es_branch])
    repo.init_submodules(overwrite=True)

    # update dodo.py with the project name
    dodo_file = repo_dir / 'dodo.py'
    with dodo_file.open('r') as f:
        dodo_contents = f.read()
    dodo_contents = dodo_contents.replace('__NAME_OF_THE_PROJECT__', project_name)
    with dodo_file.open('w') as f:
        f.write(dodo_contents)

    # rename project tex file with project_name
    src_dir = repo_dir / 'src'
    old_tex_file = src_dir / '__NAME_OF_THE_PROJECT__.tex'
    new_tex_file = src_dir / f'{project_name}.tex'
    old_tex_file.rename(new_tex_file)


if __name__ == '__main__':
    parser = gen_parser()
    args = parser.parse_args()
    gen_project(args.project_name, args.language)
