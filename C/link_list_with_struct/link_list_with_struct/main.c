#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct unit_tele
{
	char unitname[50];
	char telephone[15];
	struct unit_tele *next;
};

struct unit_tele *creat_list()
{
	struct unit_tele *q, *p, *head;
	char uname[50];
	head = q = NULL;
	while (1)
	{
		printf("Please input unit name:");
		scanf("%s", uname);
		if (strcmp(uname, "#") == 0)
			break;
		p = (struct unit_tele *)malloc(sizeof(struct unit_tele));
		printf("Please input telephone:");
		scanf("%s", p -> telephone);
		strcpy(p -> unitname, uname);
		if (q == NULL)
			head = q = p;
		else
		{
			q -> next = p;
			q = p;
		}
	}
	q -> next = NULL;
	return head;
}

void print_list(struct unit_tele *head) 
{
	struct unit_tele *p;
	for (p = head; p != NULL; p = p -> next)
		printf("%s, %s\n", p -> unitname, p -> telephone);
}

struct unit_tele *delete_list(struct unit_tele *head, char uname[])
{
	struct unit_tele *q, *p;
	for (p = head, q = NULL; p != NULL; q = p, p = p -> next)
		if (strcmp(p -> unitname, uname) == 0)
			break;
	if (p != NULL)
	{
		if (q == NULL)
			head = p->next;
		else
			q->next = p->next;
		free(p);
	}
	return head;
}

struct unit_tele *insert_list(struct unit_tele *head, char uname[], char tele[])
{
	struct unit_tele *q, *p;
	for (q = head; q != NULL; q = q->next)
		if (strcmp(q->unitname, uname) == 0)
			break;
	if (q == NULL)
	{
		p = (struct unit_tele *)malloc(sizeof(struct unit_tele));
		strcpy(p -> unitname, uname);
		strcpy(p -> telephone, tele);
		p->next = head;
		head = p;
		//free(p);
	}
	return head;
}

void query_list(struct unit_tele *head, char uname[])
{
	struct unit_tele *p;
	for (p = head; p != NULL; p = p->next)
		if (strcmp(p->unitname, uname) == 0)
			break;
	if (p != NULL)
		printf("unit_name: %s, telephone: %s\n", p->unitname, p->telephone);
	else
		printf("No this unit\n");
	return;
}

int main(void) 
{
	struct unit_tele *head;
	char uname[50], tele[15];
	head = creat_list();
	print_list(head);
	printf("input unit_name for delete:");
	scanf("%s", uname);
	head = delete_list(head, uname);
	printf("input unit_name for query:");
	scanf("%s", uname);
	query_list(head, uname);
	printf("input unit_name and it's telephone for insert:");
	scanf("%s %s", uname, tele);
	head = insert_list(head, uname, tele);
	printf("input unit_name for delete:");
	scanf("%s", uname);
	head = delete_list(head, uname);
	print_list(head);
	return 0;
}