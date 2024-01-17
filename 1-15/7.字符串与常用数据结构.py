import random


def generate_code(code_len=4):
    """
    随机生成一个验证码(包括数字与字母),位数可指定
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        # 随机获取一个数字长度(在all_chars长度值中),该随机数会重复  若不要重复,可以使用sample函数
        index = random.randint(0, last_pos)
        # 通过随机的长度值获得对应的字符并加入code实例中
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    print(pos)
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(generate_code())
    # print(get_suffix(filename="123.yaml"))


