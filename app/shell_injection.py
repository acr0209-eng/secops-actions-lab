import subprocess


def run_command(cmd):
    allowed_commands = {
        "whoami": ["/usr/bin/whoami"],
        "date": ["/usr/bin/date"],
    }

    args = allowed_commands.get(cmd)
    if args is None:
        raise ValueError("Command not allowed")

    subprocess.run(args, check=True)  # noqa: S603
