import os
from fnmatch import fnmatch


def f_path(cur_dir, file):
    return os.path.abspath(os.path.join(cur_dir, file))


def get_file(pattern):
    for cur_dir, sub_dirs, files in os.walk('.'):
        yield from (f_path(cur_dir, f) for f in files if fnmatch(f, pattern))


def pygrep(pattern, keyword):
    for file in get_file(pattern):
        try:
            with open(file) as f:
                yield from ((i, line, file) for i, line in enumerate(f) if keyword in line)
        except UnicodeDecodeError:
            print('Unicode error. Skip file %s' % file)


if __name__ == '__main__':
    import sys
    pattern, keyword = sys.argv[1:]
    for i, line, path in pygrep(pattern, keyword):
        print('{}\n{} => {}'.format(path, i, line))
