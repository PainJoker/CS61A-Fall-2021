(define (over-or-under num1 num2) 
    ;(cond
    ;    ((< num1 num2) -1)
    ;    ((= num1 num2) 0)
    ;    (else 1)
    ;)
    (if (< num1 num2) 
        -1
        (if (= num1 num2)
            0
            1
        )
    )
)

(define (make-adder num) 
    ;(lambda (inc) (+ inc num))
    (define (adder inc)
        (+ inc num)
    )
    adder
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define lst 
    ;(cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
    ;'((1) 2 (3 4) 5)
    (list (cons 1 nil) 2 (cons 3 (cons 4 nil)) 5)
)

(define (remove item lst) 
    (filter (lambda (ele) (not (= ele item))) lst)
)
