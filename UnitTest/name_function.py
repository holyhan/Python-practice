def get_formatted_name(first, last, middle=''):
    """将姓名合并，并在中间添加空格，然后将
    它们的首字母大写，再返回结果"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
