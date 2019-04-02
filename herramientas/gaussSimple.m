% Solves for Ax = b, using Simple Gauss Elimination

function gaussSimple(A, b)
    format short;
    file_id = fopen('gaussSimple.txt', 'w');
    fdisp(file_id, "SIMPLE GAUSS ELIMINATION METHOD");
    fdisp(file_id, "Phase 0:");
    Ab = [A,b];
    fdisp(file_id, Ab);
  
    %check det(A)

    n = columns(A);

    for i = 1:n-1
        for j = i+1:n
            alpha = Ab(j,i)/Ab(i,i);
            for k = i:n+1
                Ab(j,k) = Ab(j,k) - alpha*Ab(i,k);
            endfor
        endfor
        msg = strcat("Phase ",num2str(i));
        fdisp(file_id, msg);
        fdisp(file_id, Ab);
    endfor

    x(n,n) = Ab(n,n+1) / Ab(n,n);
    for i = n-1:-1:1
        acum = 0;
        for p = i+1:n
            acum = acum + Ab(i,p) .* x(p,p);
        endfor
        x(i,i) = (Ab(i,n+1)-acum)/Ab(i,i);
    endfor
    format long;
    fdisp(file_id, "x");
    fdisp(file_id, x);
    fclose(file_id);
endfunction