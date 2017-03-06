#!/usr/bin/python
"""An Ansible module to query the Apt package cache."""

from ansible.module_utils.basic import AnsibleModule
import apt

def main():
    """Run the module."""

    module = AnsibleModule(
        argument_spec=dict(
            package=dict(default=None, aliases=['pkg', 'name'], type='str')
            ),
        required_one_of=[['name']]
        )

    cache = apt.Cache()
    packages = {}
    package = module.params['package']

    try:
        if package == "all":
            for pkg in apt.Cache():
                if cache[pkg.name].is_installed:
                    pkgver = cache[pkg.name].installed
                    packages[pkg.name] = pkgver.version
            module.exit_json(changed=False, package_info=packages)
        else:
            if cache[package].is_installed:
                pkgver = cache[package].installed
                packages[package] = pkgver.version
                installed = True
            else:
                packages[package] = ""
                installed = False
            module.exit_json(changed=False, package_info=packages, installed=installed)
    except KeyError:
        message = "The package '%s' was not found in the apt-cache" % package
        installed = False
        module.exit_json(msg=message, installed=installed)
if __name__ == '__main__':
    main()
