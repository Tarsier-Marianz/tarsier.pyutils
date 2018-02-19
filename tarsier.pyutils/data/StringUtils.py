import re

class StringUtils():
    def non_alphanumeric(self, string):
        return ''.join(ch for ch in string if ch.isalnum())

    def trim_spaces(self, string):
        return re.sub('\s+',' ', string.strip())

    def is_notEmpty(self, s):
        return bool(s and s.strip())

    def is_existInList(self, mlist, mval):
        return mval in mlist

    def is_contains(self, str, keyword):
        if str.find(keyword) != -1:
            return True
        else:
            return False

    def is_containsUnicode(self, s):
        try:
            s.encode('ascii')
        except UnicodeEncodeError:
            return False
        else:
            return True

    def safe_str(self, obj):
        try:
            return str(obj)
        except UnicodeEncodeError:
            # obj is unicode
            return unicode(obj).encode('unicode_escape')