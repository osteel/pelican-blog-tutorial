from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'vagrant@192.168.72.3:22'
env.key_filename = '/home/vagrant/.ssh/insecure_private_key'
root_path = '/var/www'
log_path = '/var/log'
dest_path = '~/dev'
sitename = 'blog'
symlink_folder = 'output'

# Git repository
git_repository = 'git@github.com:osteel/pelican-blog-tutorial.git'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


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
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

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
def provision():
    if run('nginx -v', warn_only=True).failed:
        sudo('apt-get -y install nginx')
    put('./.provision/blog.conf', '/etc/nginx/sites-available/blog.conf', use_sudo=True)
    sudo('rm -f /etc/nginx/sites-enabled/blog.conf')
    sudo('ln -s /etc/nginx/sites-available/blog.conf /etc/nginx/sites-enabled/blog.conf')
    sudo('service nginx restart')

    if run('test -d %s/%s' % (log_path, sitename), warn_only=True).failed:
        sudo('mkdir %s/%s' % (log_path, sitename))

    if run('test -d %s' % root_path, warn_only=True).failed:
        sudo('mkdir %s' % root_path)

    if run('git -v', warn_only=True).failed:
        sudo('apt-get install -y git-core')

    if run('pip --version', warn_only=True).failed:
        run('wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py -P /tmp/')
        sudo('python /tmp/get-pip.py')
        run('rm /tmp/get-pip.py')

    if run('fab --version', warn_only=True).failed:
        sudo('pip install Fabric')

    if run('virtualenv --version', warn_only=True).failed:
        sudo('pip install virtualenv')
        sudo('pip install virtualenvwrapper')
        with prefix('WORKON_HOME=$HOME/.virtualenvs'):
            with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
                run('mkvirtualenv %s' % sitename)

@hosts(production)
def publish():
    if run('cat ~/.ssh/id_rsa.pub', warn_only=True).failed:
        run('ssh-keygen -N "" -f ~/.ssh/id_rsa')
        key = run('cat ~/.ssh/id_rsa.pub')
        prompt("Add this key to your Git repository and then hit return:\n\n%s\n\n" % key)

    if run('test -d %s' % dest_path, warn_only=True).failed:
        run('mkdir %s' % dest_path)

    with cd(dest_path):
        if run('test -d %s' % sitename, warn_only=True).failed:
            run('mkdir %s' % sitename)
            with cd(sitename):
                run('git clone %s .' % git_repository)
                if run('test -d %s' % symlink_folder, warn_only=True).failed:
                    run('mkdir %s' % symlink_folder)
                sudo('ln -s %s/%s/%s %s/%s' % (dest_path, sitename, symlink_folder, root_path, sitename))

        with cd(sitename):
            run('git reset --hard HEAD')
            run('git pull origin master')
            with prefix('WORKON_HOME=$HOME/.virtualenvs'):
                with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
                    run('workon blog')
                    run('pip install -r requirements.txt')
                    run('fab preview')
