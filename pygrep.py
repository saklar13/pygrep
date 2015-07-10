import os
from fnmatch import fnmatch


def f_path(dir, file):
    return os.path.abspath(os.path.join(dir, file))


def get_file(pattern):
    for cur_dir, sub_dirs, files in os.walk('.'):
        files = (f for f in files if fnmatch(f, pattern))
        yield from (f_path(cur_dir, file) for file in files)


def find_in_file(file, keyword):
    with open(file) as f:
        yield from filter(lambda l: keyword in l[1], enumerate(f))


def pygrep(pattern, keyword):
    for file in get_file(pattern):
        for i, line in find_in_file(file, keyword):
            print('{}\n{} => {}'.format(file, i, line))


if __name__ == '__main__':
    import sys
    pygrep(*sys.argv[1:])
