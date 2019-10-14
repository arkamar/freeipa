from __future__ import absolute_import

from ipaplatform.base.paths import BasePathNamespace

class GentooPathNamespace(BasePathNamespace):
    ETC_GENTOO_RELEASE = "/etc/gentoo-release"

paths = GentooPathNamespace()
