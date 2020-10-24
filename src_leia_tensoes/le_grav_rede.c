#include <stdio.h>             
#include <unistd.h>
#include <stdlib.h>
#include <string.h>  
#include <time.h>
#include <string.h>

/*
$ gpio mode 1 pwm   // configura GPIO.1 ou BCM-18 como pwm ou função alternativa alt 5
$ gpio pwm-ms       // configura o pwm para mark-space
$ gpio pwmc 10     // configura a frequencia do pwm (750hz)
$ gpio pwmr 256     // configura o ratio, neste caso para uma resolução de 8 bits
*/

void setup_pwm(void)
{
  /* faca o setup do ADC com system call do gpio */  
  system("gpio mode 1 pwm"); // configura pwm 
  system("gpio pwm-ms");
  system("gpio pwmc 10");    // 750hz
  system("gpio pwmr 256");   // conversor 8 bits
  system("gpio pwm 1 0");    // escreve 0 no pwm 
}


void mapea_pinos(void)
{
 system("gpio export 27 in"); // exporta GPIO.2 para /sys/class/gpio/gpio27/value  
 system("gpio export 22 in"); // exporta GPIO.3 para /sys/class/gpio/gpio22/value
} 

int leia_gpio_rede(void)
{
 FILE *f3;
 int x;
 char c;
 f3=fopen("/sys/class/gpio/gpio22/value","r"); fscanf(f3, "%c", &c);fclose(f3); 
 return(c-'0');
}

void grava_valor_rede(int a)
{
 FILE *f3;
 f3=fopen("/home/pi/src/src_monitoramento_remoto/src_leia_tensoes/rede.log","w"); 
 fprintf(f3,"%03d\n",a);
 fclose(f3);
}


void escreve_pwm(int i)
{ 
 char str1[50];
 char str2[50];
 strcpy(str1, "gpio pwm 1 ");
 sprintf(str2,"%d",i); 
 strcat(str1,str2); 
 system(str1); 
}

int leia_adc(void)
{
 int i=0;
 int valor=0;
 escreve_pwm(0);  
 int dummy=0x80;
 while (i<8)
 { 
   escreve_pwm(dummy+valor);
   usleep(10000);  // 10 mil micro espera filtrar e estabilizar
   if(leia_gpio_rede()==1) {valor = valor + dummy;}
   i++;
   dummy=dummy >> 1;
 }
 return(valor);
}

int adc_rede(void)
{
 return( (220*leia_adc())/100) ;
}

// char bateria[5];
// char rede[4];
int main(void)
{
 int b;
 setup_pwm();
 mapea_pinos();
 while(1)
 {
  b=adc_rede();
  printf("%03d\n",b);
  grava_valor_rede(b);
  sleep(1);
 }
}


