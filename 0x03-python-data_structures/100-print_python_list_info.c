#include <Python.h>

/**
 * print_python_list_info - prints a basic information about a Python list
 * @p: pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
	size_t size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %lu: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
