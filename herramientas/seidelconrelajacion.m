% METODO ITERATIVO DE GAUSS SEIDEL CON RELAJACION

clc  %permite borrar el area de trabajo
clear  %permite borrar las variables almacenadas
format long %permite utilizar la maxima capacidad de la maquina


fprintf('                           METODO ITERATIVO DE GAUSS SEIDEL CON RELAJACION\n\n\n');
%fprintf me permite ingresar comentarios de manera textual que pueden
%orientar al usuario en el uso del programa

%input es un comando de solicitud de entrada de datos del usuario.
a=input('Ingrese la matriz de coeficientes:\n ');
b=input('\nIngrese los t�rminos independientes:\n ');
x=input('\nIngrese el vector con las aproximacimaciones Iniciales:\n ');
iter=input('\nIngrese el n�mero m�ximo de iteraciones:\n ');
tol=input('\nIngrese la tolerancia:\n ');
w=input('\nIngrese el landa de la relajacion:\n ');

k=norm(a)*norm(a^-1);%Se calcula el condicional de la matriz de coeficientes
disp('condicional=')
disp(k)
% la funcion disp nos permite imprimir una variable en el espacio de trabajo
determinante=det(a); %se calcula el determinante de la matriz de coeficiente

if determinante==0
disp('El determinante es cero, el problema no tiene soluci�n �nica')
end

n=length(b);%numero de elementos del vector b
d=diag(diag(a)); %obtencion de la matriz diagonal
l=d-tril(a); %obtencion de la matriz diagonal superior L
u=d-triu(a); %obtencion de la matriz diagonal inferior u
fprintf('\n     SOLUCION:\n')
fprintf('\nLa matriz de transicion de gauss seidel:\n')
Tw=((d-w*l)^-1)*((1-w)*d+w*u); % matriz de transicion de gauss con relajacion
disp(Tw)
re=max(abs(eig(Tw))) %calculo del radio espectral

if re>1
disp('Radio Espectral mayor que 1')
disp('el m�todo no converge')

return
end
fprintf('\nEl vector constante es::\n')
Cw=w*(d-w*l)^-1*b; % vector constante C, para el metodo con relajacion
disp(Cw)
i=0;

err=tol+1;
z=[i,x(1),x(2),x(3),err]; %vector que me permite graficar la tabla

while err>tol & i<iter
  
xi=Tw*x+Cw;

err=max(sqrt((xi(1)-x(1))^2+(xi(2)-x(2))^2+(xi(3)-x(3))^2));
%err=norm(Xmejor-x); %norma 2
err=max(abs(xi-x)); %norma 1
%err=norm(xi-x)/norm(xi); %norma relativa
x=xi;

i=i+1;
z(i,1)=i; 
z(i,2)=x(1); 
z(i,3)=x(2); 
z(i,4)=x(3);
z(i,5)=x(4);
z(i,6)=err;
end
fprintf('\nTABLA:\n\n    n                  x1                  x2                  x3                 x4               Error\n\n   ') 
disp(z) %impresion de la tabla.