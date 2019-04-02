% Aitken method for accelerating
% f: function, x0: intial x value, tol: tolerance, nMax: max iterations

function aitken(f, x0, tol, nMax)
    format long;    
    file_id = fopen('aitken.txt', 'w');
    fdisp(file_id, "AITKEN ACCELERATION METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "x0:");
    fdisp(file_id, x0);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    
    count = 0;
    eps = 1e-16;
    while (count < nMax)
        x1 = f(x0);
        x2 = f(x1);

        if (x1 != x2)
            lambda = abs((x2-x1)/(x1-x0));
        endif

        denominator = (x2 - x1) - (x1 - x0);

        % if (abs(denominator) < eps)
        %     fdisp(file_id,'WARNING: denominator is too small');
        %     break;
        % endif

        aitkenX = x2 - ( (x2 - x1).^2 )/denominator;
        res = strcat("i:\t ", num2str(count));
        res = strcat(res, "     x0 =\t");
        res = strcat(res, num2str(aitkenX,16));
        res = strcat(res,"   Err=\t");
        errAbs(abs(aitkenX - x2));
        res = strcat(res, num2str(errAbs,16));
        fdisp(file_id, res);

        if (abs(aitkenX - x2) < tol)
            fdisp(file_id, "Fixed Point (Approx.):");
            fdisp(file_id,aitkenX);
            fdisp(file_id, "Iteration: ");
            fdisp(file_id,count+1);
            break;
        endif

        x0 = aitkenX;

        count++;

    endwhile
    fclose(file_id);
endfunction