# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase

def CreateDatabaseConenction(dbName):
    conn = QSqlDatabase()
    