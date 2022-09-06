# algoritmos de AP1

#. Faça um algoritmo que resolva as seguintes expressões aritméticas considerando A=2, B=5 e C=10.  Mostre o resultado na tela da expressão
#A+B*C/A
#(A+B)*C/A
#(A+B*C)/A

A = 2
B = 5
C = 10

expression1 = A+B*C/A
print(expression1)

expression2 = (A+B)*C/A
print(expression2)

expression3 = (A+B*C/A
            
            print(expression3)


               #Faça um algoritmo que leia dois números reais e imprima a soma e a média aritmética desses números.

               Number1=float(input("Insert the first number: "))
               Number2=float(input("Insert the second number: "))

               soma=Number1 + Number2
               media=(Number1 + Number2)/2

               print("the sum of the numbers is: " + str(soma))
               print("The mean of the numbers is: " + str(media))
               #Faça um algoritmo que leia um número inteiro e imprima seu antecessor e seu sucessor.


               Number1=int(input("Insert a whole number: "))

               print("The next number is: " + str(Number1 + 1))
               print("The previous number is: " + str(Number1 - 1))
               #Faça um algoritmo  para calcular a média aritmética entre três números quaisquer.

               Number1=int(input("Insert a number\n"))
               Number2=int(input("Insert a second number\n"))
               Number3=int(input("Insert a last number\n"))
               mean=float((Number1+Number2+Number3)/3)
               print(f' this is the mean between them {mean}')
               #5. Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário deste funcionário.

               Employee=(input("Insert employee name\n"))
               WorkingHours=float(input("Insert Working Hours\n"))
               HourlyWage=float(input("Insert Hourly Wage\n"))

               print("The employee " + str(Employee) + \
                     " has the daily salary of: $" + str(WorkingHours*HourlyWage))
               #6. FUA para ler dois inteiros (variáveis A e B) e efetuar as operações de adição, subtração, multiplicação e divisão de A por B apresentando ao final os quatro resultados obtidos.

               Number1=int(input("Insert a number\n"))
               Number2=int(input("Insert a second number\n"))


               print("The sum of the numbers is: " + str(Number1+Number2))
               print("The subtraction of numbers is: " + str(Number1-Number2))
               print("The multiplication of numbers is: " + str(Number1*Number2))
               print("The division of the numbers is: " + str(Number1/Number2))
               #FUA para calcular a área de um triângulo, exibindo o resultado. A base e a altura são dados que devem ser lidos como entrada.

               print("Enter the values of the base and the height of a triangle")

               base=float(input("Enter the base of the triangle"))
               height=float(input("enter the height of the triangle"))

               print("The triangle area is: " + str((base*height)/2))
               #Uma loja de animais precisa de um algoritmo para calcular os custos de criação de coelhos. O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. O algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.

               Amount=int(input("Enter the rabbits amount: "))

               print("The total cost in raising " + str(Amount) + \
                     " rabbits is: $" + str((Amount*0.7)/18+10))
               #9. F.U.A para calcular o valor de lucro que um vendedor tem em um produto, com base em seu preço de custo e o preço de venda.

               cost=float(input("Enter the buying cost of the product"))
               sell=float(input("Enter the selling cost of the product"))

               print("The proffit by product is: $" + str(sell-cost))
               #F.U.A que leia o preço de um produto e a quantidade comprada e exiba para o usuário o preço que ele tem que pagar pela compra.

               ProductCost=float(input("Insert the product cost"))
               QuantityPurchased=float(input("Insert the quantity purchased"))

               print("The ammount to be payed is:$" + \
                     str(QuantityPurchased*ProductCost))
               #11.F.U.A que leia dois números e calcule qual é o resto da divisão do 1o pelo 2o número. Exiba na tela este valor final.

               Number1=int(input("Insert a number: "))
               Number2=int(input("Insert another number: "))

               print("The remaining of the division of the two numbers is: " + \
                     str(Number1 % Number2))
               #F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o número. Exiba na tela este valor final.

               Number1=int(input("Insert a number: "))
               Number2=int(input("Insert another number: "))

               division=int(Number1/Number2)

               print("The whole result of the division is: " + str(division))
