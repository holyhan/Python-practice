# import os
#
# rootDir = '.'
# for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
#     print('Found directory: %s' % dirName)
#     for name in fileList:
#         print('\t%s' % name)

import os

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
	print('Found directory: %s' % dirName)
	for fname in fileList:
		print('\t%s' % fname)
	# 移除子路径中的第一个路径
	# 如果有任何子路径显示的话
	if len(subdirList) > 0:
		del subdirList[0]
