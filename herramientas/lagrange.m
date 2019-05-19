% INTERPOLACION "POLINOMIO DE LAGRAGE"

%[2 6]
%BUENO CREO
pkg load symbolic
syms x;
clc  %permite borrar el area de trabajo
clear  %permite borrar las variables almacenadas
format long %permite utilizar la maxima capacidad de la maquina

fprintf('                     INTERPOLACION "POLINIMIO DE LAGRAGE"\n\n\n');
%fprintf me permite ingresar comentarios de manera textual que pueden
%orientar al usuario en el uso del programa

xi=input('Ingrese los puntos pertenecientes a las x: ');
yi=input('Ingrese los puntos pertenecientes a las y: ');
%input es un comando de solicitud de entrada de datos del usuario.
n=length(xi);
x=sym('x'); %esta funcion nos permite dejar la variable  'x' como simbolica
% y asi poder trabajar con ella, sin tener que asignarle un valor.
for j=1:n
    producto=1;
    for i=1:j-1
        producto=producto*(x-xi(i)); %calculo del producto 1 superior de L
    end
    producto2=1;
    for i=j+1:n
        producto2=producto2*(x-xi(i)); %calculo del producto 2 superior de L
    end
    producto3=1;
    for i=1:j-1
        producto3=producto3*(xi(j)-xi(i)); %calculo del producto 3 inferior de L
    end
    producto4=1;
    for i=j+1:n
        producto4=producto4*(xi(j)-xi(i)); %calculo del producto 4 inferior de L
    end
    L(j)=(producto*producto2)/(producto3*producto4); %calculos de las L para
    fprintf('\n L%d:\n',j-1)                 %poder hallar el polinomio
    disp(L(j)) %la funcion dispo nos permite visualizar varibles o texto
    % en el workspace
end
pn=0;
for j=1:n
    pn=pn+L(j)*yi(j); %calculo del polinomio interpolante
end
   fprintf('\n POLINOMIO INTERPOLANTE: \n')
   %disp(pn) % esta ejecucion la podemos utilizar cuando no necesitamos
   %simplicar la expresion
   pn = simplify(pn); %este comando nos permite simplificar toda la expresion
   disp(pn)
   
opc=input('\nDesea aproximar un valor (si/no): ','s');
%este comando nos permite saber si el usuario quiere obtener una
%aproximacion de un punto dado, en el polinomio que se acaba de obtener
if opc=='si'
x = '12'
%x=input('\nIngrese el punto a aproximar: ');
y=eval(pn); %evaluar el punto en el polinomio
disp('\nLa aproximacion a f(x) es:')
disp(y)
end