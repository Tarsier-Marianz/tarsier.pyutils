import re

class StringUtils():
	def as_string(self, obj):
		if isinstance(obj, str):
			return '"'+ escape(obj) +'"'
		return str(obj)
		
	_esc_regex = re.compile(r"(\"|\'|\\)")
	def escape_str(self, text):
		# This escapes any escaped single or double quote or backslash.
		x = _esc_regex.sub(r"\\\1", text)
		# This replaces any '\n' with an escaped version and a real line break.
		return re.sub(r'\n', r'\\n"\n"', x)
		
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