#include <Python.h>

/**
 * print_python_list_info - prints a basic information about a Python list
 * @p: pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %i\n", size);
	printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; ++i)
	{
		printf("Element %i: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", i, Py_TYPE(item)->tp_name);
	}
}
