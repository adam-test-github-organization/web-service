import os

from fabric.colors import green
from fabric.decorators import task
from fabric.operations import local

BASE_DIR = os.path.dirname(__file__)


@task
def check():
    print(green('\nRunning static code checkers\n'))
    local('flake8 handler.py fabfile.py common test')


@task
def test():
    print(green('\nRunning tests\n'))
    local(f'nosetests {BASE_DIR}/tests/')
