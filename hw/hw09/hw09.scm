(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    (else 1)
  )
)


(define (ordered? s)
  (cond
    ((null? (cdr s)) True)
    ((<= (car s) (cadr s)) (ordered? (cdr s)))
    (else False)
  )
)


(define (deep-map fn s)
  (cond
    ((null? s) s)
    ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
    (else (cons (fn (car s)) (deep-map fn (cdr s))))
  )
)


