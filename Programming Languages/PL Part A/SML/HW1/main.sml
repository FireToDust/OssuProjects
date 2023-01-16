

(*Constants:*)
val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
val days_before_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
val days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
(*End of constants.*)

(*Helper functions: (In this case any function that is not nessesary to the course is going here.)*)
fun date_in_month(date: int*int*int, month: int) = #2 date = month;

fun is_leap_year(year) = (year mod 4 = 0 andalso year mod 100 <> 0) orelse year mod 400 = 0;

fun append(lst1: 'a list, lst2: 'a list) = 
    if null lst1
    then lst2
    else hd lst1 :: append(tl lst1, lst2);

fun remove_matching(to_remove: ''Z, lst: ''Z list) = 
    if null lst
    then []
    else 
        if to_remove = hd lst
        then remove_matching(to_remove, tl lst)
        else hd lst :: remove_matching(to_remove, tl lst);  

fun remove_duplicates(lst: ''Z list) = 
    if null lst
    then []
    else hd lst :: remove_duplicates(remove_matching(hd lst, tl lst));

(*End of helper functions.*)

(*Start of problem functions.*)

fun is_older(date1: int*int*int, date2: int*int*int) = 
    (*Check the equality of their (years, months, days), 
    if they arent equal, then the result would be which (year, month, day) is greater, 
    otherwize continue this on the next smallest*)
    if #1 date1 <> #1 date2
    then #1 date1 < #1 date2
    else 
        if #2 date1 <> #2 date2
        then #2 date1 < #2 date2
        else 
            if #3 date1 <> #3 date2
            then #3 date1 < #3 date2
            else false;

(*Im not using tail recursion yet, as that is later in the course.*)


fun number_in_month(dates: (int*int*int) list, month: int) = 
    if null dates
    then 0
    else 
        if date_in_month(hd dates, month)
        then 1 + number_in_month(tl dates, month)
        else number_in_month(tl dates, month);

fun number_in_months(dates: (int*int*int) list, months: int list) =
    if null months
    then 0
    else number_in_month(dates, hd months) + number_in_months(dates, tl months);

fun dates_in_month(dates: (int*int*int) list, month: int) = 
    if null dates
    then []
    else 
        if date_in_month(hd dates, month)
        then hd dates :: dates_in_month(tl dates, month)
        else dates_in_month(tl dates, month);

fun dates_in_months(dates: (int*int*int) list, months: int list) =
    if null months
    then []
    else append(dates_in_month(dates, hd months), dates_in_months(dates, tl months));

(*Domain: Lists with length greater than or equal to the index. Positive indexes.*)
fun get_nth(lst: 'a list, index: int) = 
    if index <= 1
    then hd lst
    else get_nth(tl lst, index - 1);

fun date_to_string(date: int*int*int) = 
    get_nth(months, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)

(*Domain: Int list with total sum greater or equal to sum.*)
fun number_before_reaching_sum(sum: int, lst: int list) = 
    if (hd lst) >= sum 
    then 0
    else 1 + number_before_reaching_sum(sum - (hd lst), tl lst);

fun what_month(day: int) = number_before_reaching_sum(day, days_before_months);

fun month_range(day1: int, day2: int) = 
    if day1>day2
    then []
    else what_month(day1)::(month_range(day1+1, day2));

fun oldest(dates: (int*int*int) list) = 
    if null dates
    then NONE
    else 
        let
            fun inner(inner_dates: (int*int*int) list) = 
                if null (tl inner_dates)
                then hd inner_dates
                else
                    let 
                        val tl_max = inner(tl inner_dates)
                    in
                        if is_older(hd inner_dates, tl_max)
                        then hd inner_dates
                        else tl_max
                    end
        in
          SOME(inner(dates))
        end;

fun number_in_months_challange(dates: (int*int*int) list, months: int list) =
    number_in_months(dates, remove_duplicates(months));
    
fun dates_in_months_challange(dates: (int*int*int) list, months: int list) =
    dates_in_months(dates, remove_duplicates(months));

fun reasonable_date(date: (int*int*int)) = 
    #1 date >= 1 andalso
    #2 date >= 1 andalso
    #2 date <= 12 andalso
    #3 date >= 1 andalso
    (if #2 date = 2 andalso is_leap_year(#1 date)
    then #3 date <= 29
    else #3 date <= get_nth(days_in_months, #2 date)) 

(*End of problem functions.*)