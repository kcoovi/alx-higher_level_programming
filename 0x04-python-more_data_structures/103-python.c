#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list - print python list
 * @p: pointer
 */
void print_python_list(PyObject *p)
{
long int size, i;
PyListObject *list = (PyListObject *)p;

printf("Python list\n");
if (!PyList_Check(p))
{
printf(" Invalid Object\n");
return;
}

size = PyList_GET_SIZE(p);
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);
for (i = 0; i < size; i++)
printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
/**
 * print_python_bytes - print python bytes
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
long int size, i;
char *str;
PyBytesObject *bytes = (PyBytesObject *)p;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR]t\n");
return;
}

size = PyBytes_Size(p);
str = bytes->ob_sval;
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);
if (size < 10)
printf("  first %ld bytes:", size + 1);
else
printf("  first 10 bytes:");
for (i = 0; i <= size && i < 10; i++)
printf(" %02x", str[i] & 0xff);
printf("\n");
}
