#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <stdarg.h> //定义参数不确定的函数需要包含的头文件

void fun(int a, ...) //a代表的是放入参数的个数
{
	va_list ap;
	va_start(ap, a);
	printf("First: %d\n", va_arg(ap, int));
	printf("Second: %f\n", va_arg(ap, double)); //在使用未知参数个数函数传入浮点数时，需要使用double类型来读取浮点数
	printf("Third: %d\n", va_arg(ap, int));
}

int main(void)
{
	//参数不确定的函数
	fun(3, 12, 34.3, 56);
	//printf("%f", 13.2);


	//realloc将已经申请好的一段大小的内存空间从新申请一个大的或者小的内存空间
	/*int *p = (int *)malloc(12);
	if (p)
		printf("%u\n", _msize(p));

	p = (int *)realloc(p, 20);
	if (p)
		printf("%u\n", _msize(p));

	free(p);
	p = NULL;*/


	//calloc在申请空间时自动将所有元素初始化为0
	/*int *p = (int*)calloc(5, sizeof(int)); //calloc在申请空间时自动将所有元素初始化为0
										   //第一个参数是元素个数，第二个参数是元素字节大小
	for (int i = 0; i < 5; i++)
		printf("p[%d] = %d\n", i, p[i]);

	free(p);
	p = NULL;*/


	//malloc和二维数组指针
	/*int(*p)[2][3] = (int(*)[2][3])malloc(sizeof(int) * 2 * 3);
	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			(*p)[i][j] = i + j;
			printf("p[%d][%d] = %d\n", i, j, (*p)[i][j]);
		}
	}

	free(p);
	p = NULL;*/


	//malloc和一维数组指针
	/*int (*p)[5] = (int(*)[5])malloc(sizeof(int) * 5);
	for (int i = 0; i < 5; i++)
	{
		(*p)[i] = i;
		printf("p[%d] = %d\n", i, (*p)[i]);
	}
	free(p);
	p = NULL;*/


	//malloc 内存大小的申请
	/*//int *p = (int *)malloc(sizeof(int)); //malloc申请空间不能初始化，需要申请之后手动对指针进行赋值
	int *p = (int *)malloc(sizeof(int) * 5); //申请一个大小为5的数组
	memset(p, 0, 40); //内存赋值，按字节来赋值
					  //第一个参数是赋值的起始地址
					  //第二个参数是每个字节的需要赋值的值
					  //第三个参数是赋值的字节数
					  //头文件是<memory.h>或<string.h>
	for (int i = 0; i < 10; i++)
		printf("p[%d] = %d\n", i, p[i]);
	free(p);
	p = NULL; //指针释放之后，一定要将指针赋值成空
			  //因为如果不赋值成空，该指针会一直指向申请的空间地址，可以读但是不能写，会导致内存越界*/


	//二维数组与指针
	/*int a[2][3] = {{1, 2, 3}, {4, 5, 6}};

	int (*p0)[3] = &a[1];
	//*(p0 - 1) == a[0]
	int (*p)[2][3] = &a;

	int (*q)[3] = a;

	int i, j;

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
			printf("a[%d][%d] = %d\n", i, j, (*p)[i][j]);
	}

	//printf("%d, %d, %d\n", (*p0)[2], (*(p0 + 1))[1], p0[1][1]);
	printf("%d, %d, %d\n", (*p0)[2], (*(p0 - 1))[1], (*p)[1][2]);*/


	//数组指针
	/*int a[5] = { 4, 3, 4, 2, 6 };
	int *p = &a[2];
	int (*p1)[5] = &a;

	printf("%p, %p, %p, %p, %p, %d\n", a, &a, p1, *p1, p1[1], (*p1)[1]);*/


	//指针数组, 拉链结构
	/*int b[3] = {1, 2, 3},
		c[2] = {4, 5},
		d[4] = {6, 7 ,8, 9},
		e[5] = {10, 11, 12, 13, 14},
		f[2] = {15, 16};

	int *a[5] = { b, c, d, e, f}; //*a[5] == *(a[5])
	printf("d[2] = %d\n", a[2][2]);*/

	//二级指针
	/*int a = 12;
	int *p = &a;

	int **p1 = &p;

	printf("%p, %p\n", p1, &p);
	printf("%p, %p\n", *p1, p);
	printf("%d, %d\n", **p1, a);*/

	//一级指针遍历数组
	/*int a[5] = { 9, 7, 5, 3, 1 };
	int *p = a;
	
	printf("%p, %p, %p, %p, %p\n", p, p + 1, a, &a[0], &a[1]);

	for (int i = 0; i < 5; i++)
	{
		printf("a[%d] = %d\n", i, p[i]); //a[i] == p[i]————下标运算符
	}*/

	return 0;
}