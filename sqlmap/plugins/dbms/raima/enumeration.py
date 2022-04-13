#!/usr/bin/env python

"""
Copyright (c) 2006-2022 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.data import logger
from plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def getBanner(self):
        warnMsg = "on Raima Database Manager it is not possible to get the banner"
        logger.warn(warnMsg)

        return None

    def getCurrentUser(self):
        warnMsg = "on Raima Database Manager it is not possible to enumerate the current user"
        logger.warn(warnMsg)

    def getCurrentDb(self):
        warnMsg = "on Raima Database Manager it is not possible to get name of the current database"
        logger.warn(warnMsg)

    def isDba(self, user=None):
        warnMsg = "on Raima Database Manager it is not possible to test if current user is DBA"
        logger.warn(warnMsg)

    def getUsers(self):
        warnMsg = "on Raima Database Manager it is not possible to enumerate the users"
        logger.warn(warnMsg)

        return []

    def getPasswordHashes(self):
        warnMsg = "on Raima Database Manager it is not possible to enumerate the user password hashes"
        logger.warn(warnMsg)

        return {}

    def getPrivileges(self, *args, **kwargs):
        warnMsg = "on Raima Database Manager it is not possible to enumerate the user privileges"
        logger.warn(warnMsg)

        return {}

    def getDbs(self):
        warnMsg = "on Raima Database Manager it is not possible to enumerate databases (use only '--tables')"
        logger.warn(warnMsg)

        return []

    def searchDb(self):
        warnMsg = "on Raima Database Manager it is not possible to search databases"
        logger.warn(warnMsg)

        return []

    def searchTable(self):
        warnMsg = "on Raima Database Manager it is not possible to search tables"
        logger.warn(warnMsg)

        return []

    def searchColumn(self):
        warnMsg = "on Raima Database Manager it is not possible to search columns"
        logger.warn(warnMsg)

        return []

    def search(self):
        warnMsg = "on Raima Database Manager search option is not available"
        logger.warn(warnMsg)

    def getHostname(self):
        warnMsg = "on Raima Database Manager it is not possible to enumerate the hostname"
        logger.warn(warnMsg)

    def getStatements(self):
        warnMsg = "on Raima Database Manager it is not possible to enumerate the SQL statements"
        logger.warn(warnMsg)

        return []
