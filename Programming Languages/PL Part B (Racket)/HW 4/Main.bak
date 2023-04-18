
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

(define get-at (compose car list-tail))

(define (sequence low high stride)
  (if (> low high)
      empty
      (cons low (sequence (+ low stride) high stride))))

(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix)) xs))

(define (list-nth-mod xs n)
  (cond [(negative? n) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [else
         (get-at xs                              ; Get object at 0 based position
                 (remainder n (length xs)))]))  ; The position is the remainder of n / the length of xs


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
                                         (cons (- counter) (add1 counter))      ;(Output . State)
                                         (cons counter (add1 counter)))) 1))    ;(Output . State)

(define dan-then-dog
  (generate-stream (lambda (is_dan) (if is_dan
                                        (cons "dan.jpg" #f)              ;(Output . State)
                                        (cons "dog.jpg" #t))) #t))       ;(Output . State)

(define (stream-add-zero s)
  (generate-stream (lambda (stream)
                     (let ([stream-next (stream)])
                       (cons (cons 0 (car stream-next))                  ;Output
                             (cdr stream-next))))                        ;State               
                   s))

(define (cycle-lists xs ys)
  (generate-stream (lambda (indexes)
                     (cons (cons (get-at xs (car indexes))                    ;Output
                                 (get-at ys (cdr indexes)))
                           (cons (if (>= (car indexes) (sub1 (length xs)))    ;State
                                     0
                                     (add1 (car indexes)))
                                 (if (>= (cdr indexes) (sub1 (length ys)))
                                     0
                                     (add1 (cdr indexes))))))
                   (cons 0 0)))

; Instead of making the assoc function, the assoc function just uses this find function which is exactly the same except it returns index instead of the pair.
; I did this so I can reuse vector-find in cached-assoc.

(define (vector-assoc v vec)
  (letrec ([inner (lambda (index)
                    (if (< index (vector-length vec))
                        (let ([index-value (vector-ref vec index)])
                          (if (and (pair? index-value) (equal? (car index-value) v))
                              index-value
                              (inner (add1 index))))
                        #f))])
    (inner 0)))



(define (cached-assoc xs n)
  (let* ([cache (make-vector n #f)]
        [current 0]
        [inner-assoc (lambda (v)
                       (let ([cache-value (vector-assoc v cache)])
                         (if cache-value
                             cache-value
                             (let ([xs-value (assoc v xs)])
                               (if xs-value
                                   (begin (print "Entered main list.")
                                          (vector-set! cache current xs-value)
                                          (if (>= current (sub1 n))
                                              (set! current 0)
                                              (set! current (add1 current)))
                                          xs-value)
                                   #f)))))])
    inner-assoc))

(get-at (list 1 2 3) 0)
(define instance (cycle-lists (list 1 2 3) (list 1 2 3 4)))
(stream-for-n-steps dan-then-dog 2)
(stream-for-n-steps instance 10)

