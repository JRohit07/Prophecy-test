from setuptools import setup, find_packages
setup(
    name = 'REL_PY_DONOT_OPEN',
    version = '1.0',
    packages = find_packages(include = ('pythonorganization.donot.openme12*', )) + ["prophecy_config_instances"],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py']},
    description = 'workflow',
    install_requires = ['numpy==1.22.*', 'pandas>=1.4.2', 'torch==1.11.0', 'matplotlib==3.5.2', 'scipy>=1.6.3,<=1.8.1', 'requests~=2.28.0',
     'prophecy-libs==1.4.7'],
    entry_points = {
'console_scripts' : [
'main = pythonorganization.donot.openme12.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
