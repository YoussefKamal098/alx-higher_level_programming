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
	double value;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str);
}

/**
 *  print_python_bytes - prints a basic information about a Python bytes
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	size_t i, length, size;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	length = size + 1 > 10 ? 10 : size + 1;

	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes: ", length);

	for (i = 0; i < length; i++)
	{
		printf("%02hhx%s", str[i]);

		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - prints a basic information about a Python list
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	size_t i, size;
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

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %lu: %s\n", i, list->ob_item[i]->ob_type->tp_name);

		if (strcmp(list->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(list->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}
