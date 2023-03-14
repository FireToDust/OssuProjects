
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

(define (sequence low high stride)
  (if (>= low high)
      empty
      (cons low (sequence (+ low stride) high stride))))

(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix)) xs))

(define (list-nth-mod xs n)
  (cond [(negative? n) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [else
         (car (list-tail xs                              ; Get object at 0 based position
                         (remainder n (length xs))))]))  ; The position is the remainder of n / the length of xs


(define (stream-for-n-steps s n)
  (define pair (s))
  (if (<= n 0)
      empty
      (cons (car pair) (stream-for-n-steps (cdr pair) (sub1 n)))))


;; Generates a stream based on a function fn where each call of fn takes a value and produses a pair of:
;; 1: The output of the stream at that point
;; 2: The the next fn input (state)
(define (generate-stream fn fn_state)
  (define result (fn fn_state))
  (thunk (cons (car result) (generate-stream fn (cdr result)))))

(define funny-number-stream
  (generate-stream (lambda (counter) (if (= (remainder counter 5) 0)
                                         (cons (- counter) (add1 counter))
                                         (cons counter (add1 counter)))) 1))

(define dan-than-dog
  (generate-stream (lambda (is_dan) (if is_dan
                                        (cons "dan.jpg" #f)
                                        (cons "dog.jpg" #t))) #t))

(define (stream-add-zero s)
  (generate-stream (lambda (stream)
                     (let stream
                     (cons (cons 0 (car stream)) (cdr stream))) s))

(stream-for-n-steps (stream-add-zero dan-than-dog) 20)

