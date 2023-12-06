#include <Python.h>
#include <object.h>
#include <stdio.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - prints information on bytes
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int j;
	char *t_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &t_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", t_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (j = 0; j <= size && j < 10; j++)
		printf(" %02hhx", t_str[j]);
	printf("\n");
}
/**
 * print_python_list - prints information about lists
 * @p: pytthon object
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int j;
	PyListObject *list = (PyListObject *)p;
	const char *t;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (j = 0; j < size; j++)
	{
		t = (list->ob_item[j])->ob_type->tp_name;
		printf("Element %i: %s\n", j, t);
		if (!strcmp(t, "bytes"))
			print_python_bytes(list->ob_item[j]);
	}
}
