from invoke import task


@task
def generAllure(c):
    c.run("allure serve C:/Users/Nazar/Desktop/RabotyNET_pytest/report")


@task
def pylint(c):
    c.run("pylint tests")
