from invoke import task, run

@task
def build(c):
    run("nosetests --detailed-errors")

@task
def dell_allure(c):
    run("Remove-Item 'C:\Users\Nazar\Desktop\RabotyNET_pytest'")