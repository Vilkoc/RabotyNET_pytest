"""This module contains tasks for the project"""
from invoke import task


@task
def generAllure(c):
    c.run("allure serve allure-report")


@task
def pylint(c):
    c.run("pylint tests")
