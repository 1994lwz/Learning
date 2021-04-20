#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#define OK 1
#define ERROR 0

typedef int Status;
typedef float ElemType;
typedef struct
{
	ElemType e[3];
}Triplet;

Status initTriplet(Triplet &T, ElemType v0, ElemType v1, ElemType v2)
{
	T.e[0] = v0;
	T.e[1] = v1;
	T.e[2] = v2;
	return OK;
}

Status destoryTriplet(Triplet &T)
{
	return OK;
}

Status getElem(Triplet T, int i, ElemType &e)
{
	if (i < 1 || i > 3)
		return ERROR;
	else
		e = T.e[i - 1];
	return OK;
}

Status putElem(Triplet &T, int i, ElemType e)
{
	if (i < 1 || i > 3)
		return ERROR;
	else
		T.e[i - 1] = e;
	return OK;
}

Status isAscending(Triplet T)
{
	return (T.e[0] <= T.e[1] && T.e[1] <= T.e[2]);
}

Status isDescending(Triplet T)
{
	return (T.e[0] >= T.e[1] && T.e[1] >= T.e[2]);
}

ElemType getMax(Triplet T)
{
	int i;
	ElemType e = T.e[0];
	for (i = 1; i < 3; i++)
		if (T.e[i] > e)
			e = T.e[i];
	return e;
}

ElemType getMin(Triplet T)
{
	int i;
	ElemType e = T.e[0];
	for (i = 1; i < 3; i++)
		if (T.e[i] < e)
			e = T.e[i];
	return e;
}

int main(void)
{
	Status flag;
	ElemType v0, v1, v2;
	Triplet T;
	printf("input v0, v1, v2:");
	scanf("%f %f %f", &v0, &v1, &v2);
	flag = initTriplet(T, v0, v1, v2);
	printf("flag = %d, T.e[0] = %4.2f, T.e[1] = %4.2f, T.e[2] = %4.2f\n", flag, T.e[0], T.e[1], T.e[2]);
	if (isAscending(T))
		printf("isAscending\n");
	if (isDescending(T))
		printf("isDescending\n");
	printf("max = %4.2f, min = %4.2f\n", getMax(T), getMin(T));
	return OK;
}