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

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
