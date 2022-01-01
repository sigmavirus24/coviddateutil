import sys

import nox


nox.options.sessions = ["test-3.10", "lint"]
nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.10"])
def test(session):
    session.install(".", "pytest")
    session.run("pytest", *session.posargs)


@nox.session
def lint(session):
    session.install(".")
    session.install("-r", "lint-requirements.txt")
    session.run("black", "src/coviddateutil", "test/", "noxfile.py")
    session.run("flake8", "src/coviddateutil", "test")
    # session.run("pylint", "src/coviddateutil", "test")
    session.run("mypy", "src/coviddateutil")
    session.run("bandit", "-r", "src/coviddateutil")
    session.run("python", "-m", "build")
    session.run("twine", "check", "dist/*")


@nox.session
def venv(session):
    session.install(".", "ptpython")
    if not session.posargs:
        session.run("ptpython")
        return
    session.run(*session.posargs)
