from invoke import task, run

@task
def build(c):
    run("nosetests --detailed-errors")

@task
def pylint(c):
    c.run("pylint tests")

@task
def generAllure(c):
    c.run("allure serve allure-results")