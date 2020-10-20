#! /usr/bin/python3
from subprocess import run
from os import path, environ, chdir, getcwd, chmod
from sys import exit

def require_env(name: str) -> str:
  value = environ.get(name)
  if value: return value
  print(f'::error ::Missing mandatory environment variable {name}')
  exit(1)

def run_git(*args: str):
  command = ['git', *args]
  print('🙮', command)
  status = run(command).returncode
  if status != 0: exit(status)

release_tag = require_env('RELEASE_TAG')
commit_author_name = require_env('COMMIT_AUTHOR_NAME')
commit_author_email = require_env('COMMIT_AUTHOR_EMAIL')
auth_username = require_env('AUTH_USERNAME')
auth_password = require_env('AUTH_PASSWORD')
url = f'https://github.com/pacman-repo-builder/pacman-repo-builder/releases/download/{release_tag}/build-pacman-repo-x86_64-unknown-linux-gnu'
print('🛈 Release Tag:', release_tag)
print('🛈 Binary URL:', url)

root = path.dirname(__file__)
chdir(root)
work_dir = getcwd()
print('🛈 Current Working Directory:', work_dir)

print('Updating Dockerfile...')
with open('Dockerfile', 'w') as dockerfile, open('Dockerfile.template', 'r') as template:
  dockerfile_content = template.read().replace('<BINARY_URL>', url)
  dockerfile.write(dockerfile_content)

print('Configuring git authentication...')
with open('auth-data.tmp', 'w') as auth_data:
  auth_data.write(f'username={auth_username}\n')
  auth_data.write(f'password={auth_password}\n')
with open('auth-prog.tmp', 'w') as auth_prog:
  auth_prog.write('#! /bin/bash\n')
  auth_prog.write('set -o errexit -o pipefail -o nounset\n')
  auth_prog.write(f'cd {work_dir}\n')
  auth_prog.write('cat auth-data.tmp\n')
  auth_prog.write('rm auth-data.tmp\n')
chmod('auth-prog.tmp', 0o777)
run_git('config', 'credential.helper', path.join(work_dir, 'auth-prog.tmp'))

print('Updating git repo...')
run_git('config', 'user.name', commit_author_name)
run_git('config', 'user.email', commit_author_email)
run_git('add', '-v', 'Dockerfile')
run_git('commit', '-m', release_tag)
run_git('tag', release_tag)
run_git('push', 'origin', '--tags', 'master')
