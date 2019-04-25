function valVectProp(A)    

    A = [-3 2 1;
         1 0 10;
         10 -2 4;];

    n=length(A);
    temp=zeros(n);
    coef=zeros(1,n);
    poten=zeros(n,1);
    
    for i=1 :n
        temp = A^i;
        poten(i) = trace(temp);
    endfor

    coef(1) =- poten(1);

    for i=2:n
        coef(i) =- poten(i)/i;
        for j=1 :i-1
            coef(i) = coef(i) - coef(j) * poten(i - j) / i;
        endfor
    endfor

    raiz = roots([1 coef]);
    valProp = diag(raiz);
    vectProp = zeros(n);
    tempvap = -1.*A(2:n,1);
    tempvep = zeros(n,1); 
    
    for i=1 :length(valProp)
        temp = A(2:n,2:n) - valProp(i,i) * eye(n-1); 
        tempvep = [1 (temp\tempvap)']; 
        vectProp(1:n,i) = tempvep/norm(tempvep);
    endfor

    disp(' ');
    disp('Valores proprios');
    disp(diag(valProp));
    disp(' ');
    disp('Vectores proprios');
    disp(vectProp);
    disp(' ');
endfunction
