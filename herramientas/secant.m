

function secant(f, x0, x1, tol, nMax) 

    format long;    
    file_id = fopen('secant.txt', 'w');
    fdisp(file_id, "SECANT METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "Domain: ");
    fdisp(file_id, [x0, x1]);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);


    y0 = f(x0);
    y1 = f(x1);
    count = 0;
    res = strcat("i:\t ", num2str(count));
    res = strcat(res, "     x0 =\t");
    res = strcat(res, num2str(x0,16));
    res = strcat(res,"   f(xi)=\t");
    res = strcat(res, num2str(y0,16));
    res = strcat(res,"   Err=\t");
    fdisp(file_id, res);
    count++;
    res = strcat("i:\t ", num2str(count));
    res = strcat(res, "     x0 =\t");
    res = strcat(res, num2str(x1,16));
    res = strcat(res,"   f(xi)=\t");
    res = strcat(res, num2str(y1,16));
    res = strcat(res,"   Err=\t");
    fdisp(file_id, res);
    count++;
    do
        x=x1-y1*(x1-x0)/(y1-y0);
        y=f(x);
        x0 = x1;
        x1 = x;
        y0 = y1;
        y1 = y;
        res = strcat("i:\t ", num2str(count));
        res = strcat(res, "     x0 =\t");
        res = strcat(res, num2str(x,16));
        res = strcat(res,"   f(xi)=\t");
        fxi = abs(y1);
        errAbs = abs(x0-x1);
        res = strcat(res, num2str(fxi,16));
        res = strcat(res,"   Err=\t");
        res = strcat(res, num2str(errAbs,16));
        fdisp(file_id, res);
        count++;
    until (abs(y1) <= tol || count >= nMax)
    
    x=x1-y1*(x1-x0)/(y1-y0);
    y=f(x);
    x0 = x1;
    x1 = x;
    y0 = y1;
    y1 = y;
    res = strcat("i:\t ", num2str(count));
    res = strcat(res, "     x0 =\t");
    res = strcat(res, num2str(x,16));
    res = strcat(res,"   f(xi)=\t");
    fxi = abs(y1);
    errAbs = abs(x0-x1);
    res = strcat(res, num2str(fxi,16));
    res = strcat(res,"   Err=\t");
    res = strcat(res, num2str(errAbs,16));
    fdisp(file_id, res);
    count++;

    fdisp(file_id, "Root (Approx.):");
    fdisp(file_id, x);
    fdisp(file_id, "Total Iterations:");
    fdisp(file_id, count);
    fclose(file_id);

endfunction