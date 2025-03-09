#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int choice;
int idx = 0;
float a, b;
char op;

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
}

void what()
{
	FILE *f = fopen("flag.txt", "r");
		if (f == NULL)
	{
	printf("File flag.txt does not exist, please contact admin");
		return;
	}
	char flag[0x100];
	fgets(flag, 0x100, f);
	puts(flag);
}

void menu()
{
	puts("1. Calculate");
	puts("2. Read");
	puts("3. Exit");
}

void calculate() {
	puts("\n1. Addition");
	puts("2. Substraction");
	puts("3. Multiplication");
	puts("4. Division");
}

void vuln() {
	long arr_size = 8;
	float calc[arr_size];
	
    	puts("Just a simple calculator. What can go wrong?");
	while (1) {
		memset(&b, 0, sizeof(b));
		menu();

		printf("Enter your choice: ");
		scanf("%d", &choice);

		if (choice == 1) {
			if (arr_size > 0x100) {
				puts("HACKING ATTEMPT DETECTED! 😡");
				exit(0);
			}
			if (idx > arr_size) {
				puts("No more, thank you!");
				continue;
			}
			calculate();
			printf("Enter your operation choice: ");
			scanf("%d", &choice);

			printf("Enter first operand: ");
			scanf("%f", &calc[idx]);
			a = calc[idx];

			printf("Enter second operand: ");
			scanf("%f", &b);

			if (choice == 1){
				calc[idx] += b;
				op = '+';
			}
			else if (choice == 2){
				calc[idx] -= b;
				op = '-';
			}
			else if (choice == 3){
				calc[idx] *= b;
				op = '*';
			}
			else {
				calc[idx] /= b;
				op = '/';
			}
			printf("The result of %.2f %c %.2f stored in idx %d.\n\n", a, op, b, idx);
			idx++;
		}
		else if (choice == 2){
			printf("Choose idx to read: ");
			scanf("%d", &choice);
			
			if (choice > idx) {
				puts("No no.");
			}
			else {
				printf("Result: %a\n\n", calc[choice]);
			}
		}
		else {
			puts("Bye bye~");
			return;
		}
	}
}

int main() {
	init();
	vuln();
	return 0;
}

