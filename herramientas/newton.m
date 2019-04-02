
function newton(f, fd, x0, tol, nMax)
    x = 1;
    while (1) + (x) != (1)
        eps = x;
        x = (x) / (2);
    endwhile
    while (eps) + (1) != (1)
        epss = eps;
        eps = (eps) / (1.0005);
    endwhile
    while (epss) + (1) != (1)
        eps1 = epss;
        epss = (epss) / (1.000005);
    endwhile
    while (eps1) + (1) != (1)
        eps2 = eps1;
        eps1 = (eps1) / (1.0000000001);
    endwhile
    while (eps2) + (1) != (1)
        eps3 = eps2;
        eps2 = (eps2) / (1.00000000000001);
    endwhile
    eps = eps3;

    format long;    
    file_id = fopen('newton.txt', 'w');
    fdisp(file_id, "NEWTON METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "Function f':");
    fdisp(file_id, fd);
    fdisp(file_id, "x0:");
    fdisp(file_id, x0);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);

    y = f(x0);
    yd = fd(x0);
    count = 0;
    res = strcat("i:\t ", num2str(count));
    res = strcat(res, "     x0 =\t");
    res = strcat(res, num2str(x0,16));
    res = strcat(res, "     f(xi) =\t");
    res = strcat(res, num2str(f(x0),16));
    res = strcat(res,"   Err=\t");
    fdisp(file_id, res);
    count = 1;
    while (count < nMax || abs(yd) > eps)
        if (count > nMax)
            fdisp(file_id, "Error: Explosion");
            break;
        endif
        x1 = x0;
        x0 = (x0 - (y/yd)); %forward newton calc
        y = f(x0);
        yd= fd(x0);

        res = strcat("i:\t ", num2str(count));
        res = strcat(res, "     x0 =\t");
        res = strcat(res, num2str(x0,16));
        res = strcat(res, "     f(xi) =\t");
        res = strcat(res, num2str(f(x0),16));
        res = strcat(res,"   Err=\t");
        errAbs = abs(x1 - x0);
        res = strcat(res, num2str(errAbs,16));
        fdisp(file_id, res);


        if(abs(x1 - x0) <= tol)
            fdisp(file_id, "Root (Approx.):");
            fdisp(file_id, x0);
            fdisp(file_id, "Total Iterations:");
            fdisp(file_id, count);
            break;
        endif
        count++;
    endwhile
    fclose(file_id);
endfunction