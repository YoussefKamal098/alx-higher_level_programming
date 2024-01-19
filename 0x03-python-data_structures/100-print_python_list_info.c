#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: Pointer to a Python list
 */
void print_python_list_info(PyObject *p)
{
	size_t size, alloc, i;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; ++i)
	{
		printf("Element % lu: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", i, Py_TYPE(item)->tp_name);
	}
}
