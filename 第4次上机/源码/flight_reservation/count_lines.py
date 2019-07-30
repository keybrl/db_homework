import os

# Scan all files in this directory.
PATH = 'D:/Code/My Code'
# I only open text files that can be opened with this encoding.
FILE_ENCODING = 'utf-8'

LANGUAGE_LIST = (
    # ('file suffix', 'language name'),
    ('.c', 'C'),
    ('.cpp', 'C++'),
    ('.cxx', 'C++'),
    ('.h', 'C/C++ Header Files'),
    ('.hpp', 'C++ Header Files'),
    ('.py', 'Python'),
    ('.md', 'Markdown'),
    ('.txt', 'Text'),
    ('.ini', 'Config Files'),
    ('.conf', 'Config Files'),
    ('.yml', 'Config Files'),
    ('.json', 'JSON'),
    ('.html', 'HTML'),
    ('.css', 'CSS'),
    ('.js', 'JavaScript'),
)
IGNORE_FILES = (
    'jquery.js',
    'jquery.min.js',
    'jquery.slim.js',
    'bootstrap.js',
    'bootstrap.min.js',
    'vue.js',
    'vue.min.js',
    'layui.js',
    'layui.min.js',
    'bootstrap.css',
    'bootstrap.min.css',
    'layui.css',
    'layui.min.css',
)

counter = dict()


def check_file(file_url, suffix, language):
    if suffix == file_url[-len(suffix):]:
        try:
            with open(file_url, 'r', encoding=FILE_ENCODING) as fp:
                print('Checked! ' + file_url)
                one_line = fp.readline()
                while one_line:
                    counter[language] = [0, 0] if not counter.get(language) else counter[language]
                    counter[language][0] += 1
                    counter[language][1] += len(one_line)
                    one_line = fp.readline()
        except:
            print('Can\'t open "' + file_url + '"')


for path in os.walk(PATH):
    for file_name in path[2]:
        if file_name in IGNORE_FILES:
            print('Ignore! ' + path[0] + '/' + file_name)
            continue
        for lang in LANGUAGE_LIST:
            check_file(path[0] + '/' + file_name, lang[0], lang[1])


print('===== Summary =====')
if '__main__' == __name__:
    for key, val in counter.items():
        print('%s: %d lines, %d characters.' % (key, val[0], val[1]))
