#include "main.h"
/**
 * print_line - print a line
 * @n: variable
 * Return: 0
 */
void print_line(int n)
{
	int a = 0;

	while (a < n && n > 0)
	{
	putchar('_');
		a++;
	}
	putchar('\n');
}
