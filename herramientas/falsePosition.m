
function falsePosition(f, xl, xr, tol, Nmax)
    format long;    
    file_id = fopen('falsePosition.txt', 'w');
    fdisp(file_id, "FALSE POSITION METHOD");
    fdisp(file_id, "Function:");
    fdisp(file_id, f);
    fdisp(file_id, "Domain:");
    fdisp(file_id, [xl,xr]);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    

    fxl = f(xl);
    fxr = f(xr);
    xm = ((xl*fxr) - (xr*fxl))/(fxr - fxl);
    fxm = f(xm);
    count = 0;
    res = strcat("i: \t", num2str(count));
    res = strcat(res, "     x0 =\t");
    res = strcat(res, num2str(xm,16));
    res = strcat(res, "     f(xi) =\t");
    res = strcat(res, num2str(fxm,16));
    res = strcat(res,"   Err=\t");
    errAbs = abs(xr -xm);
    
    fdisp(file_id, res);
    count = 1;
    if abs(fxl) <= tol
        fdisp(file_id,[xl]);
    else
        if abs(fxr) <= tol
            fdisp(file_id,[xr]);
        else
            while(count < Nmax && errAbs > tol)
                if ((fxl*fxm) < 0)
                    xr = xm;
                    fxr = f(xr);
                    xm = ((xl*fxr) - (xr*fxl))/(fxr - fxl);
                    fxm = f(xm);
                else
                    xl = xm;
                    fxl = f(xl);
                    xm = ((xl*fxr) - (xr*fxl))/(fxr - fxl);
                    fxm = f(xm);
                endif
                res = strcat("i: \t", num2str(count));
                res = strcat(res,"  xl=\t");
                res = strcat(res,num2str(xl,5));
                res = strcat(res, "     x0 =\t");
                res = strcat(res, num2str(xm,16));
                res = strcat(res,"  xr=\t");
                res = strcat(res,num2str(xr,5));
                res = strcat(res, "     f(xi) =\t");
                res = strcat(res, num2str(fxm,16));
                res = strcat(res,"   Err=\t");
                errAbs = abs(xr -xm);
                res = strcat(res, num2str(errAbs,16));
                fdisp(file_id, res);
                count++;
            endwhile
        endif
    endif
    fdisp(file_id, "Root (Approx.):");
    fdisp(file_id, xm);
    fdisp(file_id, "Iteration: ");
    fdisp(file_id,count);
    if (abs(fxm) > tol)
        fdisp(file_id, "TOLERANCE NOT REACHED: MAX ITERATIONS");
    endif
    fclose(file_id);
endfunction