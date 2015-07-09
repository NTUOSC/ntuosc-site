from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
env.deploy_repo = 'https://github.com/NTUOSC/ntuosc.github.io.git'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Sass configurations
env.sass_source = 'themes/ntuosc/scss'
env.sass_target = 'themes/ntuosc/static/css'
env.sass_imports = 'vendor/foundation/scss'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )

def github():
    local('pelican -s publishconf.py')
    with cd(env.deploy_path):
        local('ghp-import . -r github -b master && '
              'git push github master'.format(**env))

def sass(action='compile', force='no', style='compressed', sourcemap='none'):
    args = ['sass']
    if force != 'no':
        args.append('-f')
    if env.sass_imports:
        args += ['-I %s' % path for path in env.sass_imports.split(';')]
    args.append('-t {style}'.format(style=style))
    args.append('--sourcemap={type}'.format(type=sourcemap))
    args.append('--watch' if action == 'watch' else '--update')
    args.append('{sass_source}:{sass_target}'.format(**env))
    local(' '.join(args))
