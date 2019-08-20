from invoke import task, run
from config import TOMCAT_PATH, TIMEOUT
from time import sleep

@task
def build(c):
    run("nosetests --detailed-errors")

@task
def pylint(c):
    c.run("pylint tests")

@task
def generAllure(c):
    c.run("allure serve allure-results")

@task
def restart_tomcat(c):
    c.cd(TOMCAT_PATH)
    c.run("shutdown.bat")
    sleep(TIMEOUT)
    c.run("startup.bat")
    sleep(40)

@task
def run_pytest_with_allure(c):
    run('pytest -rA --alluredir report')

@task
def runTests(c):
    restart_tomcat(c)
    run_pytest_with_allure(c)
    generAllure(c)

@task
def r(c):
    print(dir(c))
    print(dir(c.run))


