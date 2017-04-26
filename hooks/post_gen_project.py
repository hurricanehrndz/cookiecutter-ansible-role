#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import read_user_yes_no

try:
    input = raw_input
except NameError:
    pass


folders = OrderedDict()

defaults_folder_name = 'defaults'

folders['tasks'] = {
    'question': '\nShould it have tasks? ',
}

folders['handlers'] = {
    'question': '\nShould it have handlers?',
    'hint': '  Add handler name i.e (Restart uwsgi) ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders[defaults_folder_name] = {
    'question': '\nIt should contain default variables?: ',
    'hint': '  Add variable i.e (operator: drunken_master) ',
    'action': '{}\n\n'
}

folders['meta'] = {
    'question': '\nShould it have meta info? ',
    'pre_hint': ' - Should it have dependencies? ',
    'pre_action': '\ndependencies:\n',
    'hint': '    Add dependency i.e ({role: aptsupercow, var: \'value\'}) ',
    'action': '  - {}\n'
}

folders['templates'] = {
    'question': '\nShould it have templates? ',
}

folders['files'] = {
    'question': '\nShould it have files? ',
}

ansible_role_name = '{{ cookiecutter.role_name }}'
ansible_test_framework = '{{ cookiecutter.ansible_test_framework }}'
ansible_test_driver = '{{ cookiecutter.ansible_test_driver }}'
molecule_test_folder = 'tests'
kitchen_test_folder = 'test'
ci_folder = 'ci'


def configure_continuos_integretion():
    if ansible_test_framework == 'test-kitchen':
        shutil.rmtree(molecule_test_folder)
        shutil.copyfile(os.path.join(ci_folder,
                                     ansible_test_driver,
                                     'kitchen.yml'),
                        '.kitchen.yml')
        os.remove('requirements.txt')
    else:
        shutil.rmtree(kitchen_test_folder)
        shutil.copyfile(os.path.join(ci_folder,
                                     ansible_test_driver,
                                     'molecule.yml'),
                        'molecule.yml')
        os.remove('Gemfile')

    shutil.rmtree(ci_folder)


def configure_role():
    print('\n\nROLE CONFIGURATION:\n===================')
    for folder_name, folder in folders.items():
        if read_user_yes_no(folder['question'], default_value=u'yes'):
            if 'hint' in folder:
                with open('{}/main.yml'.format(folder_name), 'a') as fp:
                    if 'pre_hint' in folder:
                        if read_user_yes_no(folder['pre_hint'],
                                            default_value=u'yes'):
                            fp.write(folder['pre_action'])
                        else:
                            continue

                    action_name = input(folder['hint'])
                    while action_name:
                        if folder_name != defaults_folder_name:
                            fp.write(folder['action'].format(action_name))
                        else:
                            fp.write(ansible_role_name.replace('.', '_') +
                                     '_' + folder['action'].format(action_name))
                        action_name = input(folder['hint'])
        else:
            shutil.rmtree(folder_name)


if __name__ == '__main__':
    configure_role()
    configure_continuos_integretion()
