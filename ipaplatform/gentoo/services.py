"""
    This is the place for Gentoo-specific service class implementation.
    It currently uses the RedHat one.
"""

from __future__ import absolute_import

from ipaplatform.redhat import services as redhat_services

gentoo_system_units = redhat_services.redhat_system_units.copy()

class GentooService(redhat_services.RedHatService):
    system_units = gentoo_system_units

def gentoo_service_class_factory(name, api=None):
    return redhat_services.redhat_service_class_factory(name, api)

class GentooServices(redhat_services.RedHatServices):
    def service_class_factory(self, name, api=None):
        return gentoo_service_class_factory(name, api)

timedate_services = redhat_services.timedate_services
service = gentoo_service_class_factory
knownservices = GentooServices()
