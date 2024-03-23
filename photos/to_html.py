# 获取./pics目录下所有图片的文件名，生成“<img src=".pics/{文件名}" style="height: 200px; margin-right: 5px;">”
# 的html代码，写入到./pics/pics.html文件中

import os

def get_file_name(path):
    file_name = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name.append(file)
    return file_name

def write_html(file_name):
    with open('html_content.txt', 'w') as f:
        for name in file_name:
            f.write('<img src="pics/2023/{0}" style="height: 300px; margin-right: 5px;">\n'.format(name))

# def rename():
#     # 按顺序将pics下的文件重命名为1，2，3，...
#     i = 1
#     for file in os.listdir('./pics'):
#         os.rename('./pics/' + file, './pics/' + str(i) + '.jpg')
#         i += 1


if __name__ == '__main__':
    # 设置当前目录为这个脚本的目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # rename()
    file_name = get_file_name('./pics/2023')
    write_html(file_name)
    print('Done!')