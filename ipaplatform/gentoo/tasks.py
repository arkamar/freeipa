'''
This module is for Gentoo-specific implementations of system tasks.
It currently uses the RadHat one.
'''

from __future__ import absolute_import

from ipaplatform.redhat.tasks import RedHatTaskNamespace

class GentooTaskNamespace(RedHatTaskNamespace):
    pass

tasks = GentooTaskNamespace()
