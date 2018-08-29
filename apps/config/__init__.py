import importlib
import os


__all__ = ['conf', ]

deploy_env = os.environ.get('DEPLOY_ENV', 'dev')
assert deploy_env in ['dev', 'test', 'prod']
conf = importlib.import_module('.{}'.format(deploy_env), __name__)
