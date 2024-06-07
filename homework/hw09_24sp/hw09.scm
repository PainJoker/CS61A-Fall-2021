(define (curry-cook formals body) 
  (if (null? formals) 
    body
    (list 'lambda (cons (car formals) nil) (curry-cook (cdr formals) body))
  )
)

(define (curry-consume curry args)
  (if (null? args)
    curry
    (begin
      (define val (car args))
      (define rest-curry (curry val))
      (curry-consume rest-curry (cdr args))
    )
  )
)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons (list 'equal? (car (cdr switch-expr)) (car option)) (cdr option)))
             (car (cdr (cdr switch-expr))))))
