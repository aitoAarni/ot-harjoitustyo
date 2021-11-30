from invoke import task


@task
def start(ctx):
	ctx.run("python3 src/start.py")

@task
def test(ctx):
	ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage runpo --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")