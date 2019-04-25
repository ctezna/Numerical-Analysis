
%matriz
a = [3 -1 1; 3 6 2; 3 3 7];
%solucion
b = [1;0;4];
%aproximacimaciones
x = [0;0;0];
%num iteraciones
iter = 100
%tolerancia
tol=1e-7

cond=norm(a)*norm(a^-1);
disp('condicional=')
disp(cond)
determinante=det(a);
if determinante==0
disp('El determinante es cero, el problema no tiene solución única')
return
end

n=length(b);%numero de elementos del vector b
d=diag(diag(a)); %obtencion de la matriz diagonal
l=d-tril(a); %obtencion de la matriz diagonal superior L
u=d-triu(a);%obtencion de la matriz diagonal inferior u
fprintf('\n     SOLUCION:\n')
fprintf('\nLa matriz de transicion de jacobi:\n')
T=d^-1*(l+u); 
disp(T)
re=max(abs(eig(T)))

if re>1
disp('Radio Espectral mayor que 1')
disp('el método no converge')
return
end
fprintf('\nEl vector constante es::\n')
C=d^-1*b;
disp(C)
i=0;
err=tol+1;
z=[i,x(1),x(2),x(3),err]; 
while err>tol & i<iter

  xi=T*x+C;
%disp(xi)
%err=norm(xi-x); %norma 2
err=max(abs(xi-x)); %norma 1
%err=norm(xi-x)/norm(xi); %norma relativa
x=xi;

i=i+1;
z(i,1)=i; 
z(i,2)=x(1); 
z(i,3)=x(2); 
z(i,4)=x(3);
z(i,6)=err;

end
fprintf('\nTABLA:\n\n    n                  x1                  x2                  x3              x4   Error\n\n   ');
disp(z)%impresion de la tabla.