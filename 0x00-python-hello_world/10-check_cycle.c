/**
 * check_cycle - checks cycles
 * @list: list
 * Return: 1 0r 0
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
		return (1);
	}
return (0);
}
