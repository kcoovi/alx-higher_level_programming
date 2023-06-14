#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - Print bytes
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
long int size, i, limit;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
char *string = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);

limit = (size >= 10) ? 10 : size + 1;
printf("  first %ld bytes:", limit);

for (i = 0; i < limit; i++)
{
printf(" %02x", (unsigned char)string[i]);
}

printf("\n");
}

/**
 * print_python_list - Print list
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
long int size, i;
size = Py_SIZE(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
PyObject *obj = list->ob_item[i];
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

if (PyBytes_Check(obj))
{
print_python_bytes(obj);
}
}
}
