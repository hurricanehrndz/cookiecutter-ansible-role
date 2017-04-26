# cookiecutter-ansible-role

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for creating
Ansible roles with user's choice of test framework, [Test-Kitchen](https://github.com/test-kitchen/test-kitchen) or
[Molecule](http://molecule.readthedocs.io). Additionally, each of the test frameworks
can be deployed with user's choice of test driver either [`Docker`](https://www.docker.com/) or [`Vagrant`](https://www.vagrantup.com/)

Please note that if you plan on using [Travis CI](https://travis-ci.org/) only
the docker driver is compatible.

## What's included in the Ansible role that's stubbed out?

A few things:

* basic folder that includes tasks, handlers, defaults, files and templates
* Test-Kitchen and Molecule targeted gitignore file
* One of two pre-configure test-framework with one of two test drivers
determined upon user's choice.

## Usage

To use this, you must first install the cookiecutter python package and any
test-framework driver (Docker, Vagrant) dependencies:

Install cookiecutter:

```bash
pip install --upgrade cookiecutter
```

Generate an Ansible role project:

```bash
cookiecutter https://github.com/hurricanehrndz/cookiecutter-ansible-role.git
```

or

```bash
cookiecutter git@github.com:hurricanehrndz/cookiecutter-ansible-role.git
```

Once the Ansible role project has been setup `cd` into it and prepare the test
environment.

If using Test-Kitchen:
```bash
bundle install
kitchen test
```

If using Molecule:
```bash
pip install -r requriments.txt
molecule test
```

**Then:**

* Initialize a repo, commit all the bits and push!
* Add the repo to your Travis CI account
* Write your awesome Ansible role
* Register your role with [Ansible Galaxy](https://galaxy.ansible.com/)

## Parameter Definitions

| Parameter | Default | Description |
|---|---|---|
| full_name  | Carlos Hernandez  | Author's name.  |
| email  | patrick@dualspark.com  | Author's email.  |
| role_name  | ansible-boilerplate  | Name of the role to be created.  |
| repo_name  | ansible-boilerplate  | Name of the repository to hold the new role being created.  |
| short_description  | Ansible role boilerplate contains all the boilerplate to create a fully-baked Ansible role.  |
| ansible_version  | 1.6.6  | Version of Ansible to use when testing the role being developed.  |
| role_hosts  | all  | Ansible configuration that indicates which hosts should have the role deployed  |
| role_use_sudo  | true  | Indicates that Ansible should use sudo when calling commands in the role definition yml file  |
| year  | 2017  | Year that repo is to be/was released  |

