#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
	PyObject *elem;
	PyListObject *list;
	long int len, i;

	len = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", len);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < len; i++)
	{
		elem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);
	}
}
