# Ansible Apt-Query Module

[![Build Status](https://travis-ci.org/george-buckerfield/ansible-apt-query.svg?branch=master)]
(https://travis-ci.org/george-buckerfield/ansible-apt-query)

An Ansible module for easy querying of the Apt package cache.

## Usage

```
# Check the installed version of openssl
- apt_query:
    name: openssl
  register: query

# Display the version
- debug: msg="{{ query.package_info['openssl'] }}"

# Do something if the version doesn't match a requirement
- name: update openssl if necessary
  apt:
    name: openssl
    state: latest
  become: yes
  when: query.package_info['openssl'] != "1.0.1f-1ubuntu2.21"
```
