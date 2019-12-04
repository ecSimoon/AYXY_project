# -*- coding: utf-8 -*-
#
#python——toole 进制转换工具 0.9
#
#dec == 十进制


def print_all(dec):

	print('二进制为: ',bin(dec))

	print('八进制为: ',oct(dec))

	print('十进制为: ',dec)

	print('十六进制为:',hex(dec))


def content_format(num,types):

    n=1

    while n == 1:
        dec = input('请输入要转换的%s进制数: '%types)

        dec = int(dec,num)
        print('二进制为: ',bin(dec))

        print('八进制为: ',oct(dec))

        print('十进制为: ',dec)

        print('十六进制为:',hex(dec))

        print('请选择\t1.继续进行%s进制转换\t 2.返回上一层'%types)

        n = int(input())




#菜单

def mune():

	print("-------------进制转换系统---------------")

	print("|       菜单                           |")                           

	print("|         1.二进制                     |")

	print("|         2.八进制                     |")

	print("|         3.十进制                     |")

	print("|         4.十六进制                   |")

	print("|         0.退出                       |")

	print("----------------------------------------")




def main_choice():

	while True:

		mune()

		choice = int(input('请输入选择'))

		if choice == 1:

			content_format(2,'二')

		if choice == 2:

			content_format(8,'八')

		if choice == 3:

			content_format(10,'十')

		if choice == 4:

			content_format(16,'十六 ')

		if choice == 0:

			print('\n\n\nWelcome to use next time😘😘😘\n\n\n\tGoodby!🤪\n\n✌️' )

			break


if __name__ == '__main__':
	main_choice()
