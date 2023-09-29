#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - Runs an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_loop(void)
{
        while (1)
        {
                sleep(1);
        }
        return (0);
}

/**
 * main - starts 5 zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_loop();

	return (EXIT_SUCCESS);
}
