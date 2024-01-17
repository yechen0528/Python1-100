import random
import string


def generate_code(code_len=4):
    """
    生成随机验证码
    :return:
    """
    # string.digits 包括所有的阿拉伯数字 string.ascii_letters 包括所有的大小写英文字母
    ALL_CHARS = string.digits + string.ascii_letters
    # ''.join()函数可以将多个字符串拼接成一个字符串.
    # random.choices(string, k) 从string这个字符串中随机取出 k个字符
    # random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，choices实现有放回抽样
    return ''.join(random.choices(ALL_CHARS, k=code_len))


if __name__ == '__main__':
    print(generate_code())