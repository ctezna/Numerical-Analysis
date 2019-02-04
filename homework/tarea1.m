% STEP 1: Epsilon 
eps0 = 1.0;
for k = 1 : 100;
    eps0 = 0.5 * eps0;
    t = 1 + eps0;
    if(t <= 1)
        eps0 = 2 * eps0;
        disp(['Valor del epsilon encontrado: ',num2str(eps0)])
        break
    end
end

% Comparation with the real epsilon
disp('Valor del epsilon real: ')
eps

% Step 2: Overflow 
maxexp = 1023;
disp('Valor más grande encontrado: ')
pow2(2-eps0,maxexp)

% Comparation with the biggest number
disp('Valor más grande real: ')
realmax

% Step 3: Underflow
minexp = -1022;
disp('Valor más pequeño encontrado: ')
pow2(1,minexp)

% Comparation with the smaller number
disp('Valor más pequeño real: ')
realmin

