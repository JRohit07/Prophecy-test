from setuptools import setup, find_packages
setup(
    name = 'EMR_Synapse',
    version = '1.0',
    packages = find_packages(include = ('emr_synapse*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.5.10'],
    entry_points = {
'console_scripts' : [
'main = emr_synapse.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
