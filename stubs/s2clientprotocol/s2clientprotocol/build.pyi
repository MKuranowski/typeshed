from subprocess import _CMD

def game_version() -> str: ...
def git_commit_hash() -> str: ...
def read_command_output(cmd: _CMD) -> list[str]: ...