#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

#define OK 1
#define ERROR 0
#define OVERFLOW -1

#define LIST_INIT_SIZE 20
#define LISTINCREMENT 5

typedef int Status;
typedef float ElemType;

typedef struct
{
	ElemType * elem;
	int length;
	int listsize;
}SqList;

Status compare(ElemType x, ElemType y)
{
	return x == y;
}

Status print(ElemType e)
{
	printf("%6.2f ", e);
	return OK;
}

Status InitList_Sq(SqList &L)
{
	//构造一个空的线性表L
	L.elem = (ElemType *)malloc(LIST_INIT_SIZE * sizeof(ElemType));
	if (!L.elem)
	{
		printf("Fail to malloc!\n");
		exit(OVERFLOW);
	}
	L.length = 0;
	L.listsize = LIST_INIT_SIZE;

	printf("Creat the list successful\n");
	return OK;
}

Status ListIsEmpty_Sq(SqList L)
{
	if (L.length == 0)
	{
		printf("This List is empty!\n");
		return 1;
	}
	else
		return 0;
}

Status ListInput_Sq(SqList &L)
{
	int i, n;
	while (1)
	{
		printf("Plese input the number of the list, the number must be less than %d:", L.listsize);
		scanf("%d", &n);
		if (n < 1 || n > 100)
			printf("invaild input, plese input again\n");
		else
			break;
	}
	printf("Please input the value of the List:");
	for (i = 0; i < n; i++)
		scanf("%f", &L.elem[i]);
	L.length = n;
	return OK;
}

Status ListInsert_Sq(SqList &L, int i, ElemType e)
{
	ElemType *p, *q, *newbase;
	if (i < 1 && i > L.length + 1)
		return ERROR;
	if (L.length >= L.listsize)
	{
		newbase = (ElemType *)realloc(L.elem, (L.listsize + LISTINCREMENT) * sizeof(ElemType));
		if (!newbase)
			exit(OVERFLOW);
		L.elem = newbase;
		L.listsize += LISTINCREMENT;
	}
	q = &(L.elem[i - 1]);
	for (p = &(L.elem[L.length - 1]); p >= q; --p)
		*(p + 1) = *p;
	*q = e;
	++L.length;
	return OK;
}

Status ListDelete_Sq(SqList &L, int i, ElemType &e)
{
	ElemType *p;
	if (ListIsEmpty_Sq(L))
		return ERROR;
	if (i < 1 || i > L.length)
		return ERROR;
	p = &(L.elem[i - 1]);
	e = *p;
	for (p = p + 1; p <= L.elem + L.length - 1; ++p)
		*(p - 1) = *p;
	--L.length;
	return OK;
}

int LocateElem_Sq(SqList L, ElemType e, Status(*compare)(ElemType, ElemType))
{
	//在顺序线性表L中查找第一个值e满足compare()的元素在线性表中的位序
	//返回查找到元素在线性表中的位置，若没有找到，返回0 
	int i = 1;
	ElemType *p = L.elem;
	if (ListIsEmpty_Sq(L))
		return ERROR;
	while (i <= L.length && !(*compare)(*p++, e))
		++i;
	if (i <= L.length)
		return i;
	else
		return ERROR;
}

Status MergeList_Sq(SqList La, SqList Lb, SqList &Lc)
{
	//已知顺序线性表La和Lb的元素按值非递减排列
	//归并La和Lb得到新的顺序线性表Lc，Lc的元素也按值非递减排列
	ElemType *pa, *pb, *pc, *pa_last, *pb_last;
	pa = La.elem;
	pb = Lb.elem;
	if (ListIsEmpty_Sq(La) || ListIsEmpty_Sq(Lb))
		return ERROR;
	Lc.listsize = Lc.length = La.length + Lb.length;
	pc = Lc.elem = (ElemType *)malloc(Lc.listsize * sizeof(ElemType));
	if (!Lc.elem)
		exit(OVERFLOW);
	pa_last = La.elem + La.length - 1;
	pb_last = Lb.elem + Lb.length - 1;
	while (pa <= pa_last && pb <= pb_last)
	{
		if (*pa <= *pb)
			*pc++ = *pa++;
		else
			*pc++ = *pb++;
	}
	while (pa <= pa_last)
		*pc++ = *pa++;
	while (pb <= pb_last)
		*pc++ = *pb++;
	return OK;
}

void DestoryList_Sq(SqList &L)
{
	free(L.elem);
	L.elem = NULL;
	printf("Destory the List successful\n");
}

Status SortList_Sq(SqList &L)
{
	if (ListIsEmpty_Sq(L))
		return ERROR;
	int i, low = 0;
	ElemType tmp;
	int high = L.length - 1;
	while (low < high)
	{
		for (i = low; i < high; i++)
		{
			if (L.elem[i] > L.elem[i + 1])
			{
				tmp = L.elem[i];
				L.elem[i] = L.elem[i + 1];
				L.elem[i + 1] = tmp;
			}
		}
		--high;
		for (i = high; i > low; i--)
		{
			if (L.elem[i] < L.elem[i - 1])
			{
				tmp = L.elem[i];
				L.elem[i] = L.elem[i - 1];
				L.elem[i - 1] = tmp;
			}
		}
		++low;
	}
	return OK;
}

Status ListTraverse_Sq(SqList L, Status(*visit)(ElemType))
{
	for (int i = 0; i < L.length; ++i)
	{
		if (!visit(L.elem[i]))
			return ERROR;
	}
	printf("\n");
	return OK;
}

int main(int argc, char *argv[])
{
	SqList L1, L2, L3;
	int i;
	ElemType e;
	printf("--------------------------------------------------------\n");

	printf("->Init the List 1\n");
	InitList_Sq(L1);
	ListInput_Sq(L1);
	printf("->Init the List 2\n");
	InitList_Sq(L2);
	ListInput_Sq(L2);

	printf("->print the List 1&2\n");
	ListTraverse_Sq(L1, print);
	ListTraverse_Sq(L2, print);

	printf("Input the value to List 1&2\n");
	printf("Please input the location and value of List 1:");
	scanf("%d %f", &i, &e);
	ListInsert_Sq(L1, i, e);
	printf("Please input the location and value of List 2:");
	scanf("%d %f", &i, &e);
	ListInsert_Sq(L2, i, e);

	printf("->print the List 1&2\n");
	ListTraverse_Sq(L1, print);
	ListTraverse_Sq(L2, print);

	printf("Delete the value of the List 1&2\n");
	printf("Please input the location of the List 1 which you want delete:");
	scanf("%d", &i);
	ListDelete_Sq(L1, i, e);
	printf("Please input the location of the List 2 which you want delete:");
	scanf("%d", &i);
	ListDelete_Sq(L2, i, e);

	printf("->print the List 1&2\n");
	ListTraverse_Sq(L1, print);
	ListTraverse_Sq(L2, print);

	printf("Find the value in the List 1&2\n");
	printf("Please input the value in the List 1 which you want find:");
	scanf("%f", &e);
	i = LocateElem_Sq(L1, e, compare);
	if (i)
		printf("The %f is location at %d\n", e, i);
	else
		printf("No this value\n");
	printf("Please input the value in the List 2 which you want find:");
	scanf("%f", &e);
	i = LocateElem_Sq(L2, e, compare);
	if (i)
		printf("The %f is location at %d\n", e, i);
	else
		printf("No this value\n");

	printf("Sort the List 1&2\n");
	SortList_Sq(L1);
	SortList_Sq(L2);

	printf("->print the List 1&2\n");
	ListTraverse_Sq(L1, print);
	ListTraverse_Sq(L2, print);

	printf("Merge the List 1&2\n");
	printf("->Init the List 3\n");
	InitList_Sq(L3);
	MergeList_Sq(L1, L2, L3);
	printf("->print the List 3\n");
	ListTraverse_Sq(L3, print);

	printf("Destory the List 1&2&3\n");
	DestoryList_Sq(L1);
	DestoryList_Sq(L2);
	DestoryList_Sq(L3);
	printf("\n--------------------------------------------------------\n");

	return 0;
}