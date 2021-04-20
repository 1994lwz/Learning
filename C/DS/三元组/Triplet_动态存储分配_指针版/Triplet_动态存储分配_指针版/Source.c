#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

#define OK 1
#define ERROR 0
#define TRUR 1
#define FALSE 0
#define OVERFLOW -1

typedef int Status;
typedef int ElemType;
typedef ElemType * Triplet;

void creatTriplet(Triplet *T)
{
	(*T) = (ElemType *)malloc(3 * sizeof(ElemType));
	if ((*T) == NULL)
	{
		printf("Failed to malloc\n");
		exit(OVERFLOW);
	}
}

Status InitTriplet(Triplet *T, ElemType v1, ElemType v2, ElemType v3)
{
	creatTriplet(T);

	*(*T) = v1;
	*(*T + 1) = v2;
	*(*T + 2) = v3;

	return OK;
}

Status DestoryTriplet(Triplet *T)
{
	free(*T);
	*T = NULL;
	return OK;
}

Status getElem(Triplet T, int i, ElemType *e)
{
	if (i < 1 || i > 3)
		return ERROR;
	*e = T[i - 1];
	return OK;
}

Status putElem(Triplet *T, int i, ElemType e)
{
	if (i < 1 || i > 3)
		return ERROR;
	*(*T + i - 1) = e;
	return OK;
}

Status isAscending(Triplet T)
{
	return (T[0] <= T[1] && T[1] <= T[2]);
}

Status isDescending(Triplet T)
{
	return (T[0] >= T[1] && T[1] >= T[2]);
}

Status getMax(Triplet T)
{
	int i;
	ElemType e = T[0];
	for (i = 1; i < 3; i++)
		if (T[i] > e)
			e = T[i];
	return e;
}

Status getMin(Triplet T)
{
	int i;
	ElemType e = T[0];
	for (i = 1; i < 3; i++)
		if (T[i] < e)
			e = T[i];
	return e;
}

int main(void)
{
	Triplet T;
	ElemType v0, v1, v2, e;
	Status flag, temp, temp1;

	printf("input v0, v1, v2:");
	scanf("%d %d %d", &v0, &v1, &v2);
	flag = InitTriplet(&T, v0, v1, v2);
	printf("flag = %d, T[0] = %d, T[1] = %d, T[2] = %d\n", flag, T[0], T[1], T[2]);

	if (getElem(T, 2, &e))
		printf("T[1] = %d\n", e);
	printf("input the reset location and value:");
	scanf("%d %d", &temp, &temp1);
	if (putElem(&T, temp, temp1))
		printf("T[0] = %d, T[1] = %d, T[2] = %d\n", T[0], T[1], T[2]);
	if (isAscending(T))
		printf("isAscending\n");
	if (isDescending(T))
		printf("isDescending\n");
	if (getMax(T))
		printf("max = %d\n", e);
	if (getMin(T))
		printf("min = %d\n", e);
	DestoryTriplet(&T);
	printf("Destory the Triplet\n");
}