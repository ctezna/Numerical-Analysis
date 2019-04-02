
function bisection(f, a, b, tol, Nmax)
    format long;
    file_id = fopen('bisection.txt', 'w');
    %file_id = fopen('bisection.txt', 'a');
    fdisp(file_id, "BISECTION METHOD");
    fdisp(file_id, "Function:");
    fdisp(file_id, f);
    fdisp(file_id, "Domain:");
    fdisp(file_id, [a,b]);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    

    fa = f(a);
    fb = f(b);
    c = 0;
    errAbs = 100;
    count = 0;
    if abs(fa) <= tol
        fdisp(file_id, a);
    else
        if abs(fb) <= tol
            fdisp(file_id, b);
        else
            c = (a+b)/2;
            fc = f(c);
            count = 0;
            res = strcat("i:\t ", num2str(count));
            res = strcat(res, "     x0 =\t");
            res = strcat(res, num2str(c,16));
            res = strcat(res,"   f(xi)=\t");
            res = strcat(res, num2str(fc,16));
            res = strcat(res,"   Err=\t");
            fdisp(file_id, res);
            errAbs = 100;
            count = 1;
            while (count < Nmax && (errAbs > tol))
                if((fa*fc) < 0)
                    b = c;
                    fb = f(b);
                    c = (a+b)/2;
                    fc = f(c);
                else
                    a = c;
                    fa = f(a);
                    c = (a+b)/2;
                    fc = f(c);
                endif
                res = strcat("i:\t ", num2str(count));
                res = strcat(res, "     x0 =\t");
                res = strcat(res, num2str(c,16));
                res = strcat(res,"   f(xi)=\t");
                res = strcat(res, num2str(fc,16));
                res = strcat(res,"   Err=\t");
                errAbs = abs(fb-fa);
                res = strcat(res, num2str(errAbs,16));
                fdisp(file_id, res);
                count++;
            endwhile
        endif
    endif
    fdisp(file_id, "Root (Approx.):");
    fdisp(file_id, c);
    fdisp(file_id, "Iteration: ");
    fdisp(file_id,count);
    if (errAbs > tol)
        fdisp(file_id, "TOLERANCE NOT REACHED: MAX ITERATIONS");
    endif
    fclose(file_id);
endfunction


    