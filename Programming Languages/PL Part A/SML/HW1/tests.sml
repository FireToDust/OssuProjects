use "Programming Languages\\PL Part A\\SML\\HW1\\main.sml";

(* Homework1 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)


val test1 = is_older ((1,2,3),(2,3,4)) = true

val test2 = number_in_month ([(2012,2,28),(2013,12,1)],2) = 1

val test3 = number_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = 3

val test4 = dates_in_month ([(2012,2,28),(2013,12,1)],2) = [(2012,2,28)]

val test5 = dates_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = [(2012,2,28),(2011,3,31),(2011,4,28)]

val test6 = get_nth (["hi", "there", "how", "are", "you"], 2) = "there"

val test7 = date_to_string (2013, 6, 1) = "June 1, 2013"

val test8 = number_before_reaching_sum (10, [1,2,3,4,5]) = 3

val test9 = what_month 70 = 3

val test10 = month_range (31, 34) = [1,2,2,2]

val test11 = oldest([(2012,2,28),(2011,3,31),(2011,4,28)]) = SOME (2011,3,31)

val test12a = number_in_months_challenge([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,2,3,3,4]) = 3
val test12b = dates_in_months_challenge ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4,4,3]) = [(2012,2,28),(2011,3,31),(2011,4,28)]

val test13a = reasonable_date((1,5,2)) = true
val test13b = reasonable_date((0,5,2)) = false
val test13c = reasonable_date((1,0,2)) = false
val test13d = reasonable_date((1,5,0)) = false
val test13e = reasonable_date((200,2,29)) = false
val test13f = reasonable_date((5,2,29)) = false
val test13g = reasonable_date((8,2,29)) = true
val test13h = reasonable_date((400,2,29)) = true
val test13i = reasonable_date((200,3,31)) = true
val test13j = reasonable_date((200,4,31)) = false

val incorrect1 = month_range (1, 100)