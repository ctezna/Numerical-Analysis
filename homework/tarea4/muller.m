
function muller(f, a, b, tol, nMax)
    format long;    
    file_id = fopen('muller.txt', 'w');
    fdisp(file_id, "MULLER'S METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "Domain:");
    fdisp(file_id, [a,b]);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);

    c = (a+b)/2;
    count = 0;
    res = 0;

    while(count < nMax)

        f1 = f(a);
        f2 = f(b);
        f3 = f(c);
        d1 = f1 - f3;   
        d2 = f2 - f3;
        h1 = a - c;
        h2 = b - c;
        a0 = f3;
        a1 = (((d2 * power(h1, 2)) - (d1 * power(h2, 2))) / ((h1 * h2) * (h1 - h2)));
        a2 = (((d1 * h2) - (d2 * h1)) / ((h1 * h2) * (h1 - h2)));
        x = ((-2 * a0) / (a1 + abs(sqrt(a1 * a1 - 4 * a0 * a2))));
        y = ((-2 * a0) / (a1 - abs(sqrt(a1 * a1 - 4 * a0 * a2))));


        if (x >= y)
            res = x + c;
        else
            res = y + c;
        endif
        wrd = strcat("i: ", num2str(count));
        wrd = strcat(wrd, "     x0 =\t");
        wrd = strcat(wrd, num2str(res,16));
        fdisp(file_id, wrd);
        if (abs(f(res)) < tol || abs(a-b) < tol)
            fdisp(file_id, "Root (Approx.):");
            fdisp(file_id, res);
            fdisp(file_id, "Iteration: ");
            fdisp(file_id, count);
        endif

        m = res * 100;
        n = c * 100;
        m = floor(m);
        n = floor(n);
        if (m == n)
            break;
        endif

        a = b;
        b = c;
        c = res;


        count++;
    endwhile
    fclose(file_id);
endfunction