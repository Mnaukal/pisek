import os
from typing import Optional

from .compile import supported_extensions


def files_are_equal(file_a: str, file_b: str) -> bool:
    """
    Checks if the contents of `file_a` and `file_b` are equal,
    ignoring leading and trailing whitespace
    """
    with open(file_a, "r") as fa:
        with open(file_b, "r") as fb:
            while True:
                la = fa.readline()
                lb = fb.readline()
                if not la and not lb:
                    # We have reached the end of both files
                    return True
                # ignore leading/trailing whitespace
                la = la.strip()
                lb = lb.strip()
                if la != lb:
                    return False


def resolve_extension(path: str, name: str) -> Optional[str]:
    """
    Given a directory and `name`, finds a file named `name`.[ext],
    where [ext] is a file extension for one of the supported languages.

    If a name with a valid extension is given, it is returned unchanged
    """
    # TODO: warning/error if there are multiple candidates
    extensions = supported_extensions()
    for ext in extensions:
        if os.path.isfile(os.path.join(path, name + ext)):
            return name + ext
        if name.endswith(ext) and os.path.isfile(os.path.join(path, name)):
            # Extension already present
            return name

    return None


def get_data_dir(task_dir):
    return os.path.join(task_dir, "data/")


def get_input_name(seed: int, subtask: int) -> str:
    # Here we have `subtask` rather than `is_hard` to allow support for contests
    # with more than two subtasks
    return f"{seed}_{subtask}.in"


def get_output_name(input_file: str, solution_name: str) -> str:
    """
    >>> get_output_name("sample.in", "solve_6b")
    'sample.solve_6b.out'
    """
    return "{}.{}.out".format(
        os.path.splitext(os.path.basename(input_file))[0], solution_name
    )
