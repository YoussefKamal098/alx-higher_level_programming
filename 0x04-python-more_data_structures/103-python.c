#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints a basic information about a Python list
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	size_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %lu: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 *  print_python_bytes - prints a basic information about a Python bytes
 * @p: pointer to a Python object
 */

void print_python_bytes(PyObject *p)
{
	size_t i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %lu bytes: ", size);

	for (i = 0; i < size; ++i)
	{
		printf("%02x", bytes->ob_sval[i]);

		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
