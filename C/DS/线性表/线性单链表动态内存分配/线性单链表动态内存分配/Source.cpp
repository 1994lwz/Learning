#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define OVERFLOW -1
#define OK 1
#define ERROR 0

typedef int Status;
typedef float ElemType;

typedef struct LNode
{
	ElemType data;
	struct LNode *next;
}LNode, *LinkList;

Status compare(ElemType x, ElemType y)
{
	return x == y;
}

Status Print(ElemType e)
{
	printf("%6.2f ", e);
	return OK;
}

Status InitList_L(LinkList &L, int n)
{
	LinkList p;
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	printf("Please enter the values of the elements in turn:");
	//LinkList tail = L;
	for (int i = 0; i < n; i++)
	{
		p = (LinkList)malloc(sizeof(LNode));
		scanf("%f", &p->data);
		p->next = L->next;
		L->next = p;
	}
	L->data = n;
	return OK;
}

int ListIsEmpty_L(LinkList L)
{
	return L->next == NULL;
}

Status ListInsert_L(LinkList &L, int i, ElemType e)
{
	int j = 0;
	LinkList s, p = L;
	while (p && j < i - 1)
	{
		p = p->next;
		++j;
	}
	if (!p || j > i - 1)
		return ERROR;
	s = (LinkList)malloc(sizeof(LNode));
	s->data = e;
	s->next = p->next;
	p->next = s;
	L->data += 1;
	return OK;
}

Status ListDelete_L(LinkList &L, int i, ElemType &e)
{
	int j = 0;
	LinkList p = L, q;
	while (p && j < i - 1)
	{
		p = p->next;
		++j;
	}
	if (!(p->next) || j > i - 1)
		return ERROR;
	q = p->next;
	p->next = q->next;
	e = q->data;
	free(q);
	return OK;
}

Status LocateElem_L(LinkList L, ElemType e, Status(*compare)(ElemType, ElemType))
{
	int i = 0;
	if (ListIsEmpty_L(L))
	{
		printf("This List is Empty!\n");
		return ERROR;
	}
		
	LinkList p = L->next;
	while (p && !(compare(p->data, e)))
	{
		p = p->next;
		i++;
	}
	if (p && i < (int)(L->data - 1))
		return i+1;
	else
		return ERROR;
}

Status MergeList_L(LinkList La, LinkList Lb, LinkList &Lc)
{
	LinkList pa, pb, pc;
	if (ListIsEmpty_L(La) || ListIsEmpty_L(Lb))
	{
		printf("Some List is Empty!\n");
		return ERROR;
	}
		
	pa = La->next;
	pb = Lb->next;
	Lc = pc = La;

	while (pa && pb)
	{
		if (pa->data >= pb->data)
		{
			pc->next = pa;
			pa = pa->next;
			pc = pc->next;
		}
		else 
		{
			pc->next = pb;
			pb = pb->next;
			pc = pc->next;
		}
	}

	pc->next = pa ? pa : pb;
	Lc->data = La->data + Lb->data;
	return OK;
}

Status DestoryList_L(LinkList &L)
{
	LinkList p;
	
	while (L)
	{
		p = L;
		L = L->next;
		free(p);
	}
	printf("Destory successful\n");
	return OK;
}

Status SortList_L(LinkList &L)
{
	if (ListIsEmpty_L(L))
	{
		printf("This List is Empty!\n");
		return ERROR;
	}
	int i, j;
	ElemType e1, e2, n = L->data;
	LinkList p;

	for (i = 0; i < n - 1; i++)
	{
		p = L->next;
		for (j = 0; j < n - 1 - i; j++)
		{
			e1 = p->data;
			e2 = p->next->data;
			if (e1 > e2)
			{
				p->data = e2;
				p->next->data = e1;
			}
			p = p->next;
		}
	}
	return OK;
}

Status ListTraverse_L(LinkList L, Status(*visit)(ElemType))
{
	if (ListIsEmpty_L(L))
	{
		printf("This List is Empty!\n");
		return ERROR;
	}
	LNode *p;
	p = L->next;
	while (p)
	{
		if (!visit(p->data))
			return ERROR;
		p = p->next;
	}
	return OK;
}

Status putElem_L(LinkList &L, int i, ElemType e)
{
	if (ListIsEmpty_L(L))
	{
		printf("This List is Empty!\n");
		return ERROR;
	}
	int j = 0;
	LinkList p;
	p = L->next;
	if (i < 0 || i > L->data)
		return ERROR;
	while (p && j < i -1)
	{
		p = p->next;
		j++;
	}
	if (!p || j > i - 1)
		return ERROR;
	else
	{
		p->data = e;
		return OK;
	}
}

Status GetElem_L(LinkList L, int i, ElemType &e)
{
	if (ListIsEmpty_L(L))
	{
		printf("This List is Empty!\n");
		return ERROR;
	}
	int j = 0;
	LinkList p = L;
	while (p && j < i)
	{
		p = p->next;
		j++;
	}
	if (!p || j > i)
		return ERROR;
	e = p->data;
	return OK;
}

int main(int argc, char *argv[])
{
	LinkList La, Lb, Lc;
	ElemType e;
	int i, n;
	printf("***************Linear single linked list test program***************\n");

	printf("***********************Initialize function**************************\n");
	printf("-> Initializes a single linked list La\n");
	printf("How many elements do you want to set for La\n");
	scanf("%d", &n);
	InitList_L(La, n);
	printf("-> Initializes a single linked list Lb\n");
	printf("How many elements do you want to set for Lb\n");
	scanf("%d", &n);
	InitList_L(Lb, n);
	printf("Initialization La and Lb successful\n\n");

	printf("**********************ListTraverse function*************************\n");
	printf("->Print the La\n");
	ListTraverse_L(La, Print);
	printf("->Print the Lb\n");
	ListTraverse_L(Lb, Print);
}