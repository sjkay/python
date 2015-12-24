;; Scheme ;;

; Q2
(define (cube x)
  (* x x x)
)


; Q3
(define (over-or-under x y)
  (cond
    ((< x y) -1)
    ((= x y) 0)
    (else 1)
  )
)


; Q4
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond
    ((= 0 a) b)
    ((= 0 b) a)
    ((= 0 (modulo a b)) b)
    ((= 0 (modulo b a)) a)
    (else (gcd (min a b) (modulo (max a b) (min a b))))
  )
)


; Q5
(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil))))
)
  

; Q6
(define (remove item lst)
  (if (null? lst)
    lst
    (if (= item (car lst))
      (remove item (cdr lst))
      (append (car lst) (remove item (cdr lst)))
    )
  )
)


; Q7
(define (filter f lst)
  (if (f (car lst))
    (append (car lst) (remove item (cdr lst)))
    (filter f (cdr lst))
  )
)


; Q8
(define (make-adder num)
  (lambda (x) (+ x num))
)


; Q9
(define (composed f g)
  'YOUR-CODE-HERE
)

