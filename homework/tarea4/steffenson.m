
function steffenson(f,p0,tol,nMax)
    format long;

    file_id = fopen('steffenson.txt', 'w');
    fdisp(file_id, "STEFFENSON ACCELERATION METHOD");
    fdisp(file_id, "Function f:");
    fdisp(file_id, f);
    fdisp(file_id, "x0:");
    fdisp(file_id, p0);
    fdisp(file_id, "Tolerance:");
    fdisp(file_id, tol);
    
    for i=0:nMax   
        p1=f(p0);
        p2=f(p1);
        p=p0-(p1-p0)^2/(p2-2*p1+p0);
        if abs(p-p0)<tol  
            break;
        endif
        p0=p;
        res = strcat("i: ", num2str(i));
        res = strcat(res, "     x0 =\t");
        res = strcat(res, num2str(p0,16));
        fdisp(file_id, res);     
    endfor
    if abs(p-p0)>tol  
        fdisp(file_id, "Failed to converge in ");
        fdisp(file_id, i);
        fdisp(file_id, "iterations.");
    endif
    if abs(p-p0)<=tol
        fdisp(file_id, "Fixed Point (Approx.):"); 
        fdisp(file_id, p0);
        fdisp(file_id, "Iteration: ");
        fdisp(file_id,i);
    endif
    fclose(file_id);
endfunction