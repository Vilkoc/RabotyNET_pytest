"""This module contains tasks for the project"""
from invoke import task


@task
def pylint(c):
    c.run("pylint tests")


@task
def generAllure(c):
    c.run("allure serve allure-results")
