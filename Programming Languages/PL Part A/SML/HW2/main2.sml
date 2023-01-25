(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

fun all_except_option(to_remove, lst) = 
    let
        fun inner(inner_lst) = 
            case inner_lst of
            [] => [] |
            hd1::tl1 =>
            if same_string(to_remove, hd1)
            then tl1
            else hd1::inner(tl1)
        
        val result = inner(lst)
    in
        if List.length(result) = List.length(lst)
        then NONE
        else SOME result
    end;

fun get_substitutions1(subs, to_sub) = 
    case subs of
    [] => [] |
    hd1::tl1 => 
        case all_except_option(to_sub, hd1) of
        NONE => get_substitutions1(tl1, to_sub) |
        SOME out => out @ get_substitutions1(tl1, to_sub);

fun get_substitutions2(subs, to_sub) =
    let
        fun inner(inner_subs, current_result) = 
            case inner_subs of
            [] => current_result |
            hd1::tl1 => 
                case all_except_option(to_sub, hd1) of
                NONE => inner(tl1, current_result) |
                SOME out => inner(tl1, out @ current_result)
    in
        inner(subs, [])
    end;

fun similar_names(subs, name) =
    case name of
    {first=fst, middle=mid, last=lst} =>
        let
            fun fill_in(name_subs, current_result) = 
                case name_subs of
                [] => current_result |
                hd1::tl1 => fill_in(tl1, {first = hd1, middle = mid, last = lst} :: current_result)
        in
            name::fill_in(get_substitutions2(subs, fst), [])
        end
    



(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)

fun card_color(card_suit, _) = 
    case card_suit of
    Clubs => Black |
    Spades => Black |
    _ => Red

fun card_value(_, card_rank) = 
    case card_rank of
    Num x => x |
    Ace => 11 |
    _ => 10

fun remove_card(cs, c, e) = 
    case cs of
    [] => raise e |
    hd1::tl1 =>
    if c = hd1
    then tl1
    else hd1::remove_card(tl1, c, e)

fun all_same_color(cards) = 
    case cards of
    [] => false |
    _::[] => true |
    hd1::hd2::tl2 => card_color(hd1) = card_color(hd2) andalso all_same_color(hd2::tl2)

fun sum_cards(cards) = 
    case cards of 
    [] => 0 |
    hd1::tl1 => card_value(hd1) + sum_cards(tl1)

fun score(held_cards, goal) = 
    let
        val sum = sum_cards(held_cards)
        val preliminary_score = 
        if sum > goal
        then 3 * (sum - goal)
        else (goal-sum)
    in
        if all_same_color(held_cards)
        then preliminary_score div 2
        else preliminary_score
    end

fun officiate(deck, moves, goal) = 
    let
        fun run(held_cards, deck, moves) = 
            case moves of
            [] => score(held_cards, goal) |
            Discard to_discard ::tl_moves =>
                run(remove_card(held_cards, to_discard, IllegalMove), deck, tl_moves) |
            Draw::tl_moves => 
                case deck of
                [] => score(held_cards, goal) |
                hd_deck::tl_deck => 
                    run(hd_deck::held_cards, tl_deck, tl_moves)          
    in
        run([], deck, moves)
    end
