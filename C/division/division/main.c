#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int len = 0;
	int a, b, dividend;
	int result[200];

	printf("Please input the a:");
	scanf("%d", &a);
	dividend = a;
	printf("Please input the b:");
	scanf("%d", &b);

	while (len < 200 && (a % b != 0))
	{
		result[len] = (a * 10) / b;
		a = (a * 10) % b;
		len++;
	}

	printf("%d / %d = 0.", dividend, b);
	for (int i = 0; i < len; i++)
	{
		printf("%d", result[i]);
	}
	printf("\n");

	return 0;
}