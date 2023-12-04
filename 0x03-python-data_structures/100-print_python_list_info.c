#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - prints information about python lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int j;
	PyObject *py;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (j = 0; j < Py_SIZE(p); j++)
	{
		printf("Element %d: ", j);

		py = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(py)->tp_name);
	}
}
