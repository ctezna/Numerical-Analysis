
function multipleRoots(f, fd, fdd, x0, tol, nMax)
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
    file_id = fopen('multipleRoots.txt', 'w');
    fdisp(file_id, "MULTIPLE ROOTS METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "Function f':");
    fdisp(file_id, fd);
    fdisp(file_id, "Function f''':");
    fdisp(file_id, fdd);
    fdisp(file_id, "x0:");
    fdisp(file_id, x0);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);

    fx = f(x0);
    fdx = fd(x0);
    fddx = fdd(x0);
    err = tol + 1;
    count = 0;
    res = strcat("i:\t ", num2str(count));
    res = strcat(res, "     x0 =\t");
    res = strcat(res, num2str(x0,16));
    res = strcat(res, "     f(xi) =\t");
    res = strcat(res, num2str(fx,16));
    res = strcat(res, "     err =\t");
    fdisp(file_id, res);
    count++;
    while (count < nMax && err > tol)
        x1 = x0;
        x0 = (x0 - ((fx * fdx) / (fdx**2 - (fx * fddx))));
        fx = f(x0);
        fdx = fd(x0);
        fddx = fdd(x0);

        err = abs(x0-x1);

        res = strcat("i:\t ", num2str(count));
        res = strcat(res, "     x0 =\t");
        res = strcat(res, num2str(x0,16));
        res = strcat(res, "     f(xi) =\t");
        res = strcat(res, num2str(fx,16));
        res = strcat(res, "     err =\t");
        res = strcat(res, num2str(err,16));
        fdisp(file_id, res);

        if(err < tol)
            fdisp(file_id, "Root (Approx.):");
            fdisp(file_id, x0);
            fdisp(file_id, "Total Iterations:");
            fdisp(file_id, count);
            fdisp(file_id, "Err:");
            fdisp(file_id, err);
            break;
        endif
        count++;
    endwhile
    fclose(file_id);
endfunction