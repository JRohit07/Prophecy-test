from setuptools import setup, find_packages
setup(
    name = 'REL_PY_PIP_SG_SRC',
    version = '1.0',
    packages = find_packages(include = ('com.sg_src.main*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.5.8'],
    entry_points = {
'console_scripts' : [
'main = com.sg_src.main.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
