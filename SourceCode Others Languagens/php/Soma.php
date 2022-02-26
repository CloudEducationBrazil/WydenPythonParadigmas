<?php

  print("Digite Número 1: "); $n1 = fgets(STDIN);
  print("Digite Número 2: "); $n2 = fgets(STDIN);
  $avarage = ((float)$n1 + (float)$n2) / 2.0;

  printf("Resultado = %.2f", $avarage);
  //echo $avarage
?>
