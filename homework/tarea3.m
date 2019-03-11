f = input("Insert Function:");
plot = input("Do you wish to plot function? (0-NO,1-YES)");
if plot == 1
    ezplot(f,[0,10]);
endif
disp("Incremental Search - f(x,y)");
x0 = input("x0:");
y0 = input("y0:");
h = input("Delta:");
tol = input("Tolerance:");
Nmax = input("Max iterations:");

function incremental2D(f, x0, y0, h, tol, Nmax)
    format long;
    file_id = fopen('roots_2D.txt', 'w');
    %file_id = fopen('incremental.txt', 'a');
    fdisp(file_id, "INCREMENTAL SEARCH 2D");
    fdisp(file_id, "Roots for function:");
    fdisp(file_id, f);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    fdisp(file_id, "Starting at (x0, y0):");
    fdisp(file_id, [x0, y0]);
    fdisp(file_id, "ROOT INTERVALUES(A-B, C-D):");

    r0 = f(x0, y0);
    if abs(r0) <= tol
        fdisp(file_id, [x0,x0,y0,y0]);
    endif

    x1 = x0 + h;
    y1 = y0 + h;
    count = 1;
    r1 = f(x1, y1);

    if abs(r1) <= tol
        fdisp(file_id, [x1,x1,y1,y1]);
    endif

    while (count < Nmax)
        if ((r0 * r1) < 0)
            A = [x0,x1,y0,y1];
            fdisp(file_id, A);
        endif
        x0 = x1;
        y0 = y1;
        x1 = x1 + h;
        y1 = y1 + h;
        r0 = f(x0,y0);
        r1 = f(x1,y1);
        count++;
    endwhile
    fclose(file_id);
endfunction

incremental2D(f,x0,y0,h,tol,Nmax);

disp("Bisection 2D Method");
disp("Reference Values in roots_2D.txt");
a = input("Insert A:");
b = input("Insert B:");
c = input("Insert C:");
d = input("Insert D:");
tol = input("Insert Tolerance:");
Nmax = input("Max iterations:");


function bisection2D(f, a, b, c, d, tol, Nmax)
    format long;
    file_id = fopen('roots_2D.txt', 'a');
    fdisp(file_id, "BISECTION 2D METHOD");
    fdisp(file_id, "Domain:");
    fdisp(file_id, [a,b,c,d]);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    fdisp(file_id, "Root located at x,y (Approx.):");

    fab = f(a,b);
    fcd = f(c,d);

    if abs(fab) <= tol
        fdisp(file_id, [a,b]);
    else
        if abs(fcd) <= tol
            fdisp(file_id, [c,d]);
        else
            mx = (a+c)/2;
            my = (b+d)/2;
            fm = f(mx,my);
            count = 1;
            while (count < Nmax && (abs(a-c) > tol) && (abs(b-d) > tol))
                if((fab*fm) < 0)
                    c = mx;
                    d = my;
                    fcd = f(c,d);
                    mx = (a+c)/2;
                    my = (b+d)/2;
                    fm = f(mx,my);
                endif
                if((fcd*fm) < 0)
                    a = mx;
                    b = my;
                    fab = f(a,b);
                    mx = (a+c)/2;
                    my = (b+d)/2;
                    fm = f(mx,my);
                endif
                count++;
            endwhile
        endif
    endif
    fdisp(file_id, [mx,my]);
    fdisp(file_id, "f(x,y) - Absolute Error: ");
    fdisp(file_id, fm);
    if ((abs(a-c) > tol) && (abs(b-d) > tol))
        fdisp(file_id, "TOLERANCE NOT REACHED: MAX ITERATIONS");
    endif
    fclose(file_id);
endfunction

bisection2D(f,a,b,c,d,tol,Nmax);