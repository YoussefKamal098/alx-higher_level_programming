#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - prints a basic information about a Python float
 * @p: pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	double d;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	d = ((PyFloatObject *)p)->ob_fval;

	printf("  value: %s\n",
	    PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_list - prints a basic information about a Python list
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	size_t size, alloc, i;
	char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %lu: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
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

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
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
