(define (my-filter func lst) 
    (cond 
        ((null? lst)
            lst)
        ((func (car lst)) 
            (cons (car lst) (my-filter func (cdr lst))))
        (else 
            (my-filter func (cdr lst)))
    )
)

(define (interleave s1 s2) 
    (define (cat s1 s2)
        (if (null? s1)
            s2
            (cons (car s1) (cat (cdr s1) s2))
        )
    )
    (cond
        ((null? s1) s2)
        ((null? s2) s1)
        (else (cat (list (car s1) (car s2)) (interleave (cdr s1) (cdr s2))))
    )
)

(define (accumulate merger start n term)
    (if (= n 0)
        start
        (accumulate merger (merger start (term n)) (- n 1) term)
    )  
)

(define (no-repeats lst) 
    (if (null? lst) 
      lst
      (cons (car lst) (no-repeats (my-filter (lambda (term) (not (= term (car lst)))) (cdr lst))))
    )
)
