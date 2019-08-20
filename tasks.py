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
    run(TOMCAT_PATH + "shutdown.bat")
    sleep(TIMEOUT)
    run(TOMCAT_PATH + "startup.bat")
    sleep(40)

@task
def run_pytest_with_allure(c):
    run('pytest -rA --alluredir report')

@task
def run_tests(c):
    restart_tomcat()
    run_pytest_with_allure


