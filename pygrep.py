import os
from fnmatch import fnmatch


def pygrep(pattern, keyword):
    for cur_dir, sub_dirs, files in os.walk('.'):
        for file in (x for x in files if fnmatch(x, pattern)):
            full_path = os.path.abspath(os.path.join(cur_dir, file))
            with open(full_path) as f:
                try:
                    yield from ((i, line, full_path) for i, line in enumerate(f) if keyword in line)
                except UnicodeDecodeError:
                    pass

if __name__ == '__main__':
    import sys
    pattern, keyword = sys.argv[1:]
    for i, line, path in pygrep(pattern, keyword):
        print('{}\n{} => {}'.format(path, i, line))
