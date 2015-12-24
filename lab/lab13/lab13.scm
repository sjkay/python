;; Tail Recursion ;;

; Q2
(define (last s)
  (if (null? (cdr s)) 
      (car s) 
      (last (cdr s))
  )
)


; Q3
(define (reverse lst)
  (if (null? lst)
      ()
      (append (reverse (cdr lst)) (list (car lst)))
  )
)


; Q5
(define (interleave-map s1 s2)
  (if (null? s1) 
    nil
    (cons-stream (car s1) (interleave-map s2 (stream-cdr s1)))
  )
)


; Q6
(define (stream-filter s pred)
  (cond
    ((null? s) nil)
    ((pred (car s)) (cons-stream (car s) (stream-filter (stream-cdr s) pred)))
    (else (stream-filter (stream-cdr s) pred))
  )
)


; Q7
(define fibs (make-fib-stream 0 1))
(define (make-fib-stream a b)
  (cons-stream a (make-fib-stream b (+ a b)))
)


(define (stream-to-list s num-elements)
  (if (or (null? s) (= num-elements 0))
    nil
    (cons (car s)
          (stream-to-list (stream-cdr s)
                          (- num-elements 1)))))
