(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ordered? s) 
    (if (null? (cdr s))
        #t
        (and (<= (car s) (cadr s)) (ordered? (cdr s)))
    )
)

(define (square x) (* x x))

(define (pow base exp) 
    (cond
        ((or (= base 1) (= base 0))
            base)
        ((= exp 0)
            1)
        ((even? exp) 
                (square (pow base (/ exp 2))))
        ((odd? exp) 
               (* base (pow base (- exp 1))))
    )
)
