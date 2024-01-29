from setuptools import setup, find_packages
setup(
    name = 'Pipeline_first',
    version = '1.0',
    packages = find_packages(include = ('pipeline_first*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.3'],
    entry_points = {
'console_scripts' : [
'main = pipeline_first.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
