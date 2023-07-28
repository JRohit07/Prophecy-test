from setuptools import setup, find_packages
setup(
    name = 'PYTHON_BASIC_FAILURE',
    version = '1.0',
    packages = find_packages(include = ('pythonbasic.test.mainone*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.5.9'],
    entry_points = {
'console_scripts' : [
'main = pythonbasic.test.mainone.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
