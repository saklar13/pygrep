import os
from fnmatch import fnmatch


def pygrep(pattern, keyword):
    for cur_dir, sub_dirs, files in os.walk('.'):
        for file in files:
            if fnmatch(file, pattern):
                full_path = os.path.join(cur_dir, file)
                with open(full_path) as f:
                    for i, line in enumerate(f):
                        if keyword in line:
                            yield full_path, i, line


if __name__ == '__main__':
    import sys
    pattern, keyword = sys.argv[1:]
    for path, i, line in pygrep(pattern, keyword):
        print('{}\n{} => {}'.format(path, i, line))
