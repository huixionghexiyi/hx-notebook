# 正则表达式 
#  这个链接很详细，推荐！
#  https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md

r'''
    module re
    Support for regular expressions (RE).

    This module provides regular expression matching operations similar to those found in Perl. It supports both 8-bit and Unicode strings; both the pattern and the strings being processed can contain null bytes and characters outside the US ASCII range.

    Regular expressions can contain both special and ordinary characters. Most ordinary characters, like "A", "a", or "0", are the simplest regular expressions; they simply match themselves. You can concatenate ordinary characters, so last matches the string 'last'.

    The special characters are:

        "."      Matches any character except a newline.  
        "^"      Matches the start of the string.  
        "$"      Matches the end of the string or just before the newline at  
                the end of the string.  
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.  
                Greedy means that it will match as many repetitions as possible.  
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.  
        "?"      Matches 0 or 1 (greedy) of the preceding RE.  
        *?,+?,?? Non-greedy versions of the previous three special characters.  
        {m,n}    Matches from m to n repetitions of the preceding RE.  
        {m,n}?   Non-greedy version of the above.  
        "\\"     Either escapes special characters or signals a special sequence.  
        []       Indicates a set of characters.  
                A "^" as the first character indicates a complementing set.  
        "|"      A|B, creates an RE that will match either A or B.  
        (...)    Matches the RE inside the parentheses.  
                The contents can be retrieved or matched later in the string.  
        (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).  
        (?:...)  Non-grouping version of regular parentheses.  
        (?P name ...) The substring matched by the group is accessible by name.  
        (?P=name)     Matches the text matched earlier by the group named name.  
        (?#...)  A comment; ignored.  
        (?=...)  Matches if ... matches next, but doesn't consume the string.  
        (?!...)  Matches if ... doesn't match next.  
        (? =...) Matches if preceded by ... (must be fixed length).  
        (? !...) Matches if not preceded by ... (must be fixed length).  
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,  
                        the (optional) no pattern otherwise.  
    The special sequences consist of "\" and a character from the list below. If the ordinary character is not on the list, then the resulting RE will match the second character.

        \number  Matches the contents of the group of the same number.  
        \A       Matches only at the start of the string.  
        \Z       Matches only at the end of the string.  
        \b       Matches the empty string, but only at the start or end of a word.  
        \B       Matches the empty string, but not at the start or end of a word.  
        \d       Matches any decimal digit; equivalent to the set [0-9] in  
                bytes patterns or string patterns with the ASCII flag.  
                In string patterns without the ASCII flag, it will match the whole  
                range of Unicode digits.  
        \D       Matches any non-digit character; equivalent to [^\d].  
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in  
                bytes patterns or string patterns with the ASCII flag.  
                In string patterns without the ASCII flag, it will match the whole  
                range of Unicode whitespace characters.  
        \S       Matches any non-whitespace character; equivalent to [^\s].  
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]  
                in bytes patterns or string patterns with the ASCII flag.  
                In string patterns without the ASCII flag, it will match the  
                range of Unicode alphanumeric characters (letters plus digits  
                plus underscore).  
                With LOCALE, it will match the set [0-9_] plus characters defined  
                as letters for the current locale.  
        \W       Matches the complement of \w.  
        \\       Matches a literal backslash.  
    This module exports the following functions:

        match     Match a regular expression pattern to the beginning of a string.  
        fullmatch Match a regular expression pattern to all of a string.  
        search    Search a string for the presence of a pattern.  
        sub       Substitute occurrences of a pattern found in a string.  
        subn      Same as sub, but also return the number of substitutions made.  
        split     Split a string by the occurrences of a pattern.  
        findall   Find all occurrences of a pattern in a string.  
        finditer  Return an iterator yielding a Match object for each match.  
        compile   Compile a pattern into a Pattern object.  
        purge     Clear the regular expression cache.  
        escape    Backslash all non-alphanumerics in a string.  
    Some of the functions in this module takes flags as optional parameters:

        A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D  
                    match the corresponding ASCII character categories  
                    (rather than the whole Unicode categories, which is the  
                    default).  
                    For bytes patterns, this flag is the only available  
                    behaviour and needn't be specified.  
        I  IGNORECASE  Perform case-insensitive matching.  
        L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.  
        M  MULTILINE   "^" matches the beginning of lines (after a newline)  
                    as well as the string.  
                    "$" matches the end of lines (before a newline) as well  
                    as the end of the string.  
        S  DOTALL      "." matches any character at all, including the newline.  
        X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.  
        U  UNICODE     For compatibility only. Ignored for string patterns (it  
                    is the default), and forbidden for bytes patterns.  
    This module also defines an exception 'error'.

    No value for argument 'string' in function callpylint(no-value-for-parameter)
    Peek Problem
    No quick fixes available
'''
r"""
    \d    :[0-9]
    \w    :[0-9a-zA-Z_]
    .     :一个任意字符
    *     :任意多个字符(包括0个)
    ?     :前面的字符出现0次或1次的字符
    +     :至少一个字符
    {n}   :n个字符
    {n,m} :n到m个字符
    \s    :匹配一个空格
    \     :转义字符，转义:{ } [ ] / \ + * . $ ^ | ?   为字符，而不是标识
    +     :匹配匹配+之前的字符出现次数>=1的任意字符串

    [0-9a-zA-Z\_]   :匹配一个数字、字母、下划线
    [0-9a-zA-Z\_]+  :匹配至少一个  数字、字母、或下划线
    [0-9a-zA-Z\_]{3,8}  :3到8个数字、字幕、下划线
    [^c]at          :不以c开头的字符串：如:mat、Zat、_at
    A|B             :或匹配，A、B是两个 子表达式
    ^               :匹配字符头，^\d  表示匹配以一个数子开头的字符串
    $               :匹配字符尾，\d$  表示匹配以一个数字结尾的字符串

    特征标群：
    (ab)*           :匹配以ab开头的字符串，空字符串也匹配
    (A|B)*          :匹配A或B开头的字符串，空字符串也匹配
"""
# ----------------------
# re模块
import re
# 匹配成功返回Match对象
print(re.match(r'^[0-9a-zA-Z]{3,8}','wqf910j20t9r1'))
print(re.match(r'^\d{3}\-\d{3,8}$', '123-112424'))
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
# ----------------------
# 切分字符串
import re
print('a b  c'.split(' '))
print(re.split(r'[\s]+','a b  c'))# 通过re库，忽略掉空格
print(re.split(r'[\s\,]+','a b , c'))# 加上逗号
print(re.split(r'[\s\,\;]+','a b , c'))# 加上分号
# ----------------------
# 分组
import re
m = re.match(r'^(\d{3})-(\d{3,8})$','010-123456')
print(m.groups())
print(m.group(0))
print(m.group(1)) # 010
print(m.group(2)) # 123456
# ----------------------
# 贪婪匹配
# 默认情况下，匹配时尽可能多的匹配
import re
m = re.match(r'(\d+)(0*)','12312500000').groups()
print(m)
# ----------------------
# 编译
# 1. 如果正则表达式的字符串本身不合法报错，报错
# 2. 用编译后的字符串去匹配
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$') # 提前编译
# 使用
m = re_telephone.match('010-123345').groups()
print(type(re_telephone))
print(m)