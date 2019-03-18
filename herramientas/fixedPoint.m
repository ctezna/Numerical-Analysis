
function fixedPoint(f, g, x0, tol, Nmax)
    format long;    
    file_id = fopen('fixedPoint.txt', 'w');
    fdisp(file_id, "FIXED POINT METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "Function g:");
    fdisp(file_id, g);
    fdisp(file_id, "x0:");
    fdisp(file_id, x0);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    
    gx = g(x0);
    errAbs = abs(gx - x0);
    count = 0;
    while ((errAbs > tol) && (count < Nmax))
       gx = g(x0);
       fx = f(gx);
       errAbs = abs(gx - x0);
       x0 = gx;
       res = strcat("i: ", num2str(count));
       res = strcat(res, "     x0 =\t");
       res = strcat(res, num2str(x0,16));
       fdisp(file_id, res);
       count++;
    endwhile
    fdisp(file_id, "Fixed Point (Approx.):");
    fdisp(file_id, x0);
    fdisp(file_id, "Total Iterations:");
    fdisp(file_id, count);
    fclose(file_id);
endfunction