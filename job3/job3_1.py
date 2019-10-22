# 实现print函数

def print_string(*text, sep=' ', end='\n'):
    textStr = ''
    if len(text) == 1:
        return textStr + text[0] + end
    for index, txt in enumerate(text):
        if index < len(text)-1:
            textStr += txt + sep
        else:
            textStr += txt
    textStr += end
    return textStr


print(print_string('This is a test')) #返回This is a test\n
print(print_string('This', 'is', 'a', 'test')) #返回This is a test\n
print(print_string('This', 'is', 'a', 'test', sep = '-'))  #返回This-is-a-test\n
print(print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.'))  #返回This_is_a_test_,_Yes.
