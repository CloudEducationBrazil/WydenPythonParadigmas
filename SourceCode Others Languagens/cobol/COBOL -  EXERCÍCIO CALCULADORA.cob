EXERCÍCIO 1 - CALCULADORA

Desenvolver um programa que receba 2 variáveis numéricas inteiras e informe:
1. o valor da soma.
2. o valor da subtração.
3. o valor da multiplicação.
4. o valor da divisão.

=====================================================================================
IDENTIFICATION DIVISION.
PROGRAM-ID.  Calculadora.
ENVIRONMENT DIVISION.
 Special-names.
 Decimal-point is comma.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
  01 DADOS.
* Declaração de variáveis: Nota 1 e Nota 2, soma, subtracao, multiplicacao e divisão
    02 W-N1    		PIC  9(03) VALUE ZEROS.
    02 W-N2    		PIC  9(03) VALUE ZEROS.
    02 W-Soma  		PIC  9(03) VALUE ZEROS.
    02 W-Subtracao        PIC  9(03) VALUE ZEROS.
    02 W-Multiplicacao    PIC  9(03) VALUE ZEROS.
    02 W-Divisao    	PIC  9(03)V99 VALUE ZEROS.
 01 MascaraInt           PIC ZZ9.
 01 MascaraFloat         PIC ZZ9,9. 
*o zzz. é a separação de um campo
* EXIBE MENSAGEM NA TELA, intereção com o usuário
  01 MENSAGEMS-DE-TELA.
    02 MENSA1    	PIC X(50) VALUE "Digite o primeiro valor:  ". 
    02 MENSA2     PIC X(50) VALUE "Digite o segundo valor:  ".
    02 MENSA3     PIC X(50) VALUE "Soma:  ".
    02 MENSA4     PIC X(50) VALUE "Subtracao:  ".
    02 MENSA5     PIC X(50) VALUE "Multiplicacao:  ".
    02 MENSA6     PIC X(50) VALUE "Divisao:  ".
    02 MENSA7 	PIC X(50) VALUE '--------FIM DO PROGRAMA----------'.
    02 MENSA8   	PIC X(30) VALUE SPACE.
 01 DATA-DO-SISTEMA.
    02 ANO       PIC 9(02) VALUE ZEROS.
    02 MES       PIC 9(02) VALUE ZEROS.
    02 DIA       PIC 9(02) VALUE ZEROS.
  SCREEN SECTION.
 01 TELA01.
    02 LINE 02 COLUMN 06 PIC 9(02)/ USING DIA.
    02 LINE 02 COLUMN 09 PIC 9(02)/ USING MES.
    02 LINE 02 COLUMN 12 PIC 9(02)  USING ANO.
    02 LINE 02 COLUMN 24 VALUE
 "XXXXX CALCULADORA XXXXX".
 PROCEDURE DIVISION.
 Inicio.
 Display "Data: " at 0201.
 ACCEPT  DATA-DO-SISTEMA FROM DATE.
 DISPLAY ERASE       AT    0101.
 DISPLAY TELA01      AT    0101.
 MOVE    ZEROS       TO    DADOS.
 Entrada.
*RECEBENDO VALORES
*Recebe o primeiro valor
 display MENSA1 AT 0630.
 accept MascaraInt AT 0921.
 move MascaraInt to W-N1.
*Recebe o segundo valor
 display MENSA2 AT 0630.
 move zeros to MascaraInt.
 accept MascaraInt AT 1021.
 move MascaraInt to W-N2.
 Calcula.   
*Calculo da soma: // usa o add
 add W-N1 W-N2 to W-Soma.

*Calculo da subrtacao: // usa subtract e o from para sub n1 do n2
 subtract W-N1 from W-N2 giving W-Subtracao.

*Calculo da multiplicacao: // usa o multiply e o by para mult o n1 do n2
 multiply W-N1 by W-N2 giving W-Multiplicacao.

*Calculo da divisao: // usa o divide e o by para div o n1 do n2
 divide W-N1 by W-N2 giving W-Divisao.
 display "-----------------------------------" at 1229.            
 display "|" at 1328.
 display "|" at 1428. 
 display "|" at 1528.  
 display "|" at 1628.  
 display "|" at 1728.   

* Exibir a Soma das variáveis.
 display MENSA3 AT 1330. 
 move W-Soma to MascaraInt.  
 display MascaraInt at 1350.
* Exibir a Subtracao das variáveis (usa-se if para colocar o número negativo).
 display MENSA4 AT 1430.
 move W-Subtracao to MascaraInt.
 if MascaraInt < 0
 display "-" at 1449
 display MascaraInt at 1450
   else
 display MascaraInt at 1450.
* Exibir a Multiplicacao das variáveis.
 display MENSA5 AT 1530.
 move W-Multiplicacao to MascaraInt.  
 display MascaraInt at 1550.
* Exibir a Divisão das variáveis.
 display MENSA6 AT 1630.
 move W-Divisao to MascaraFloat.
 display MascaraFloat at 1650.
 display "-----------------------------------" at 1829.
 display "|" at 1364.
 display "|" at 1464. 
 display "|" at 1564.  
 display "|" at 1664.  
 display "|" at 1764.   
 Finaliza.
 DISPLAY MENSA7 AT 2230.
 DISPLAY MENSA8 AT 2330.
 Stop " ".
 Stop Run.

