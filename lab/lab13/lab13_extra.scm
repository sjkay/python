;; Tail Recursion Extra ;;

; Q8
(define (insert n s)
  (cond 
    ((null? s) (list n))
    ((<= n (car s)) (append (list n) s))
    (else (append (list (car s)) (insert n (cdr s))))
  )
)


;; Streams Extra ;;

(define (stream-to-list s num-elements)
  (if (or (null? s) (= num-elements 0))
    nil
    (cons (car s)
          (stream-to-list (stream-cdr s)
                          (- num-elements 1)))))

; Q9
(define (cycle lst)
  (cond ((null? lst) ())
        ((null? (cdr lst)) (cons-stream (car lst) (cycle lst)))
        (else (cons-stream (car lst) (cons-stream (car (cdr lst)) (car (cdr (cdr lst))))))
  )
)


