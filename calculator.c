//FEEL FREE TO PUSH MORE UPDATES TO THIS


#include <stdio.h>
#include <stdlib.h>

int main()
{

//Declaration of variables

   int a, b, sum, addition, subtraction, multiplication,modulus, choice;
   float division;
   
//Printing out simple menu to user to choose from

   printf("-----------SUICIDECALC-------------\n");
   printf("         1. Addition\n ");
   printf("        2. Subtraction\n");
   printf("         3. Division\n");
   printf("         4. Multiplication\n");
   printf("         5. Modulus\n\n");


//Prompt User for Choice

printf("Enter choice : ");
scanf("%d", &choice);

//Use of while loop to reprompt user incase a value not in menu is entered

while (choice >=5 || choice <=0)
{
    printf("Please enter valid choice : ");
    scanf("%d", &choice);
}


//clear above

  system("cls");

//Use of switch to with choices corresponding to what user selects

  switch(choice)
    {
    
    case 1:
        printf("\nEnter first number: ");
        scanf("%d", &a);
        printf("Enter second number: ");
        scanf("%d", &b);
        sum = a + b;
        printf("\nYour sum is %d", sum);
        break;
    
    case 2:
        printf("Enter first number: \n");
        scanf("%d", &a);
        printf("\nEnter second number: \n");
        scanf("%d", &b);
        subtraction = a - b;
        printf("\nYour answer is %d", subtraction);
        break;
        
    case 3:
        printf("Enter first number: \n");
        scanf("%d", &a);
        printf("\nEnter second number: \n");
        scanf("%d", &b);
        division = (float)a / b;
        printf("\nYour quotient is %.2f", division);
        break;
        
    case 4:
        printf("Enter first number: \n");
        scanf("%d", &a);
        printf("\nEnter second number: \n");
        scanf("%d", &b);
        multiplication = a * b;
        printf("\nYour product is %d", multiplication);
        break;
        
    case 5:
        printf("Enter first number: \n");
        scanf("%d", &a);
        printf("\nEnter second number: \n");
        scanf("%d", &b);
        modulus = a % b;
        printf("\nYour remainder is %d", modulus);
        break;
        
        
    }
    
    return 0;
}
