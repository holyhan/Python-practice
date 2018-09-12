#!/usr/bin/env python3

import os
import sys
import hashlib

def hash_file(path, blocksize = 65536):
    '''
    计算path对应文件的MD5值，生成一个HEX摘要
    :param path: 文件路径
    :param blocksize: 每次读取文件的块大小
    :return: 文件16进制摘要
    '''
    file = open(path, 'rb')
    hasher = hashlib.md5()
    buffer = file.read(blocksize)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = file.read(blocksize)
    file.close()

    return hasher.hexdigest()

def find_duplicate_file(parent_folder):
    '''
    扫描一个路径下的所有重复文件
    :param parent_folder: 路径名
    :return: 重复文件，格式为 {hash:[names]}
    '''
    dups = {}
    for (dir_name, sub_dirs, file_list) in os.walk(parent_folder):
        print('Scanning %s...' % dir_name)
        for file_name in file_list:
            # 获取文件路径
            path = os.path.join(dir_name, file_name)
            # 计算哈希值
            file_hash = hash_file(path)
            # 添加或拼接文件路径
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]

    return dups


def join_dictionary(dict1, dict2):
    '''
    合并两个字典，将字典dict2合并到字典dict1中
    :param dict1: 目标字典，最终dict2的所有信息都会汇总到这个字典里
    :param dict2: 起始字典，最终把自身内容汇总到dict1中
    :return: 无
    '''
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def print_results(dict):
    '''
    打印重复文件结果
    '''
    # filter(func, list)配合lambda表达式用于过滤list，func返回布尔类型表示当前list
    # 元素是否可取，布尔值为真则可取，布尔值为假则不取
    results = list(filter(lambda x: len(x) > 1, dict.values()))
    if len(results) > 0:
        print('找到了重复文件：')
        print('以下文件是相同的。虽然它们的文件名不同')
        for result in results:
            for sub_result in result:
                print('\t\t%s' % sub_result)
            print('-----------------------')
    else:
        print('未找到重复文件')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        foloders = sys.argv[1:]
        for i in foloders:
            # 遍历给定文件目录
            if os.path.exists(i):
                # 如果文件路径存在，找出重复的文件并把他们拼接到dups中
                join_dictionary(dups, find_duplicate_file(i))
            else:
                print('%s 不是一个有效的路径' % i)
        print_results(dups)
    else:
        print('用法：\'python3 duplicate_find.py folder\'或\'python3 duplicate_find.py folder1 folder2 folder3\'')
