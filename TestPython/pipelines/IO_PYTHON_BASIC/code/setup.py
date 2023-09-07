from setuptools import setup, find_packages
setup(
    name = 'SamplingMode_IO_All',
    version = '1.0',
    packages = (
      find_packages(include = ('pythonbasicio.test.mainone*', ))
      + ['prophecy_config_instances.pythonbasicio.test.mainone.configall']
    ),
    package_dir = {
      'prophecy_config_instances.pythonbasicio.test.mainone.configall': 'configs/resources/pythonbasicio/test/mainone/configall'
    },
    package_data = {'prophecy_config_instances.pythonbasicio.test.mainone.configall' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.5.8'],
    entry_points = {
'console_scripts' : [
'main = pythonbasicio.test.mainone.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
