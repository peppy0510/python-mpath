# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com
'''


import os
import sys
import shutil
import string
from mstr import mstr


class mpath():

    def __init__(self, path):
        self.path = path
        self.serial = 0
        self.status = ''
        # self.remove = False
        self.isfile = os.path.isfile(path)
        self.set_path(path)
        self.original_path = self.path
        self.original_dirname = self.dirname
        self.original_filename = self.filename
        self.original_basename = self.basename
        self.original_extension = self.extension

    def revert(self):
        self.path = self.original_path
        self.dirname = self.original_dirname
        self.filename = self.original_filename
        self.basename = self.original_basename
        self.extension = self.original_extension

    def get_path(self):
        return mstr(self.path)

    def get_dirname(self):
        return mstr(self.dirname)

    def get_filename(self):
        return mstr(self.filename)

    def get_basename(self):
        return mstr(self.basename)

    def get_extension(self):
        return mstr(self.extension)

    # def set_serial(self, serial):
    #     '''
    #     serialize에 사용되는 인덱스.
    #     '''
    #     self.serial = serial

    def set_path(self, path, check_isfile=False):
        '''
        새로운 path에 기반하여 나머지 정보를 수정.
        '''
        self.path = path
        self.dirname = os.path.dirname(path)
        self.filename = os.path.basename(path)
        if not check_isfile or self.isfile:
            self.basename, self.extension = os.path.splitext(self.filename)
        else:
            self.basename, self.extension = (self.filename, '')

    def set_filename(self, filename, check_isfile=False):
        '''
        새로운 filename에 기반하여 나머지 정보를 수정.
        '''
        self.filename = filename
        if not check_isfile or self.isfile:
            self.basename, self.extension = os.path.splitext(self.filename)
        else:
            self.basename, self.extension = (self.filename, '')
        self.path = os.path.join(self.dirname, self.filename)

    def set_basename(self, basename, check_isfile=False):
        '''
        새로운 basename에 기반하여 나머지 정보를 수정.
        '''
        self.basename = basename
        if not check_isfile or self.isfile:
            self.filename = self.basename + self.extension
        else:
            self.filename = self.basename
        self.path = os.path.join(self.dirname, self.filename)

    def set_extension(self, extension, check_isfile=False):
        '''
        새로운 extension에 기반하여 나머지 정보를 수정.
        '''
        self.extension = extension
        if not check_isfile or self.isfile:
            self.filename = self.basename + self.extension
        else:
            self.filename = self.basename
        self.path = os.path.join(self.dirname, self.filename)

    def get_split(self, depth=0):
        '''
        path를 구성하는 요소들을 리턴.
        '''
        def split_dir(dirname):
            dirname = os.path.dirname(dirname)
            basename = os.path.basename(dirname)
            return dirname, basename

        elements = []
        dirbase = self.path
        for i in range(depth):
            dirbase, basename = split_dir(dirbase)
            elements.insert(0, basename)
        elements.insert(0, split_dir(dirbase)[0])
        elements = [v for v in elements if len(v) > 0]
        filename = os.path.basename(self.path)
        basename, extension = os.path.splitext(filename)
        elements += [basename, extension]
        return elements

    # def get_split(self, depth=0):

        # return mstr(self.path).path_split(depth=depth)
        # return self.dirname, self.basename, self.extension, self.isfile

    def _is_type_of_extension(self, ext):
        if self.isfile and self.extension.strip('.').lower() in ext:
            return True
        return False

    def is_audio(self):
        ext = 'wav|mp3|m4a|ogg|flac|wma|mid|cue|sfk|mp3.sfk|wav.sfk'
        return self._is_type_of_extension(ext)

    def is_video(self):
        ext = 'avi|flv|mkv|mp4|mpeg|mpg|tp|ts|vob|wmv|smi'
        return self._is_type_of_extension(ext)

    def is_image(self):
        ext = 'bmp|gif|jpeg|jpg|png'
        return self._is_type_of_extension(ext)

    def is_document(self):
        ext = 'md|doc|docx|pdf|ppt|pptx|xls|xlsx|hwp'
        return self._is_type_of_extension(ext)

    def is_executable(self):
        ext = 'exe|com|bat'
        return self._is_type_of_extension(ext)

    def is_compressed(self):
        ext = 'rar|zip|iso'
        return self._is_type_of_extension(ext)

    def is_websource(self):
        ext = 'url|htm|html|css|js'
        return self._is_type_of_extension(ext)

    def get_md5(self):
        if not os.path.isfile(self.path):
            return
        with open(self.path, 'rb') as file:
            return mstr(file.read()).get_md5()

    # def get_pattern_index(self, pattern):
    # return mstr(mstr(self.basename).get_pattern_index(pattern,
    # self.basename))

    # def get_pattern_index_from_to(self, pattern_from, pattern_to):
    # return mstr(mstr(self.basename).get_pattern_index_from_to(pattern_from,
    # pattern_to))

    # def get_pattern_removed(self, pattern):
    #     return mstr(mstr(self.basename).get_pattern_removed(pattern))

    def upper(self):
        self.set_basename(self.basename.upper())

    def upper_extension(self):
        self.set_extension(self.extension.upper())

    def lower(self):
        self.set_basename(self.basename.lower())

    def lower_extension(self):
        self.set_extension(self.extension.lower())

    def capitalize(self):
        self.set_basename(self.basename.capitalize())

    def capitalize_extension(self):
        self.set_extension(self.extension.capitalize())

    def title(self):
        basename = self.basename
        basename = basename.title()
        if len(basename) == 0:
            return basename
        newstr = [basename[0]]
        for cnt in range(1, len(basename)):
            if basename[cnt - 1].isdigit() and \
                    basename[cnt] in string.ascii_uppercase:
                newstr += basename[cnt].lower()
            else:
                newstr += basename[cnt]
        basename = ''.join(newstr)
        self.set_basename(basename)

    def insert_string(self, value, position, reverse=False):
        basename = self.basename
        if reverse:
            position = len(basename) - position
        if position < 0:
            position = 0
        if position > len(basename):
            position = len(basename)
        basename = basename[:position] + value + basename[position:]
        self.set_basename(basename)

    # def remove_duplicated_extention(self):
    #     if self.isfile is False:
    #         return
    #     base, ext = os.path.splitext(self.basename)
    #     if ext.lower() == '.' + self.extension.lower():
    #         self.set_basename(base)

    def search_subpath(self, pattern=u'*', file=True, directory=True):

        import glob

        def search_subpath(path, pattern):
            retlist = glob.glob(os.path.join(path, pattern))
            findlist = os.listdir(path)
            for p in findlist:
                nextpath = os.path.join(path, p)
                if os.path.isdir(nextpath):
                    retlist += search_subpath(nextpath, pattern)
            return retlist

        paths = search_subpath(self.path, pattern)

        if not file and directory:
            paths = [v for v in paths if os.path.isdir(v)]
        elif file and not directory:
            paths = [v for v in paths if os.path.isfile(v)]
        elif not file and not directory:
            return []
        return paths

    def remove(self, message=True):
        '''
        해당 경로 이하를 모두 삭제.
        '''
        BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(30, 38)
        path = os.path.abspath(self.path)
        if os.path.exists(path):
            if message:
                print('removing %s' % (path))
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
            except:
                colour = RED
                msg = 'failed removing %s' % (path)
                seq = '\x1b[1;%dm' % (colour) + msg + '\x1b[0m' + os.linesep
                sys.stdout.write(seq)

    def initialize(self, own='www-data:www-data', mod=755, forced=True, message=True):
        '''
        해당 경로 이하를 모두 삭제하고 새롭게 생성.
        '''
        wasdir = os.path.isdir(self.path)
        wasfile = os.path.isfile(self.path)
        if not wasdir and not wasfile:
            if len(self.extension) == 0:
                wasdir = True
            else:
                wasfile = True

        if forced:
            self.remove(message=message)

        exists = os.path.isdir(self.path) or os.path.isfile(self.path)
        if not exists and wasdir:
            if message:
                print('creating %s' % (self.path))
            os.makedirs(self.path, mod)
        elif not exists and wasfile:
            if message:
                print('creating %s' % (self.path))
            dirname = os.path.dirname(self.path)
            if not os.path.isdir(dirname):
                os.makedirs(dirname, mod)
            with open(self.path, 'w') as file:
                file.write('')
        self.change_ownmod(own=own, mod=str(mod).rjust(4, '0'))

    def remove_empty(self, parent=0):
        '''
        비어 있는 부모 디렉토리를 찾아서 삭제.
        '''
        def remove_empty(path, parent=0):
            if os.path.isdir(path) and not os.listdir(path):
                os.rmdir(path)
            if parent > 0:
                parent -= 1
                remove_empty(os.path.dirname(path), parent)

        remove_empty(self.path, parent=parent)

    def change_ownmod(self, own='www-data:www-data', mod='0755', recursive=False):
        if not os.path.exists(self.path):
            return
        if sys.platform.startswith('win'):
            return
        option = ''
        if recursive:
            option = '-R'
        import time
        import subprocess
        command = 'chmod %s %s %s' % (option, mod, self.path)
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        proc.communicate()
        time.sleep(0.05)
        command = 'chown %s %s %s' % (option, own, self.path)
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        proc.communicate()


def __test__():
    test_path = os.path.join('var', 'www', 'some.text')
    path = mpath(test_path)
    print(path.get_path())
    print(path.get_dirname())
    print(path.get_filename())
    print(path.get_basename())
    print(path.get_extension())
    print(path.get_split())
    print(path.get_split(depth=2))
    print(path.get_md5())
    path.set_extension('doc')
    print(path.get_path())

    current_path = os.path.dirname(os.path.abspath(__file__))

    test_path = os.path.join(
        current_path, '__test__', 'var', 'www', 'some.txt')
    path = mpath(test_path)
    path.initialize()
    print('-' * 50)
    searched = mpath(os.path.join(current_path, '__test__')).search_subpath('*.txt')
    for v in searched:
        print(v)
    print('-' * 50)
    path.remove()

    test_path = os.path.join(
        current_path, '__test__', 'var', 'www', 'some')
    path = mpath(test_path)
    path.initialize()
    path.remove()

    path.remove_empty(parent=4)


if __name__ == '__main__':
    from io import TextIOWrapper
    sys.stdout = TextIOWrapper(sys.stdout.buffer,
                               encoding='utf-8', errors='replace')
    __test__()
