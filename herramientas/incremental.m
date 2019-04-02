
function incremental(f, x0, h, tol, Nmax)
    format long;
    file_id = fopen('incremental.txt', 'w');
    %file_id = fopen('incremental.txt', 'a');
    fdisp(file_id, "INCREMENTAL SEARCH");
    fdisp(file_id, "Roots for function:");
    fdisp(file_id, f);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    fdisp(file_id, "Starting at x0:");
    fdisp(file_id, x0);
    fdisp(file_id, "ROOT INTERVALS:");
    r0 = f(x0);

    if abs(r0) <= tol
        fdisp(file_id, [x0,x0]);
    endif

    x1 = x0 + h;
    count = 0;
    r1 = f(x1);

    if abs(r1) <= tol
        fdisp(file_id, [x1,x1]);
    endif

    while (count < Nmax)
        if ((r0 * r1) < 0)
            A = [x0,x1];
            fdisp(file_id, A);
        endif
        x0 = x1;
        x1 = x1 + h;
        r0 = f(x0);
        r1 = f(x1);
        count++;
    endwhile
    fdisp(file_id, "Iteration: ");
    fdisp(file_id,count+1);
    fclose(file_id);
endfunction
