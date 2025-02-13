(define (curry-cook formals body) 
  (cond
    ((null? formals) body)
    (else `(lambda (,(car formals)) ,(curry-cook (cdr formals) body)))
  )
)

(define (curry-consume curry args)
  (cond 
    ((null? args) curry)
    (else (curry-consume (curry (car args)) (cdr args)))
  )
)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))
;(cons (switch) (cons expr (cons options nil)))
; expr = (+ 1 1)
; options = ((1 2) (2 4) (3 6))
; option = (1 2) (cons 1 (cons 2 nil))
(define (switch-to-cond switch-expr)
  (cons `cond 
        (map (lambda (option)
               (cons (cons `equal? (cons (car (cdr switch-expr)) (cons (car option) nil))) (cdr option))
              )
             (car (cdr (cdr switch-expr)) ; options
             )
        )
  
  )
             
)
; (cons (cons `equal? (cons (car (cdr switch-expr)) (cons (car option) (cdr option))) ) nil)
; (define (switch-to-cond switch-expr)
;   (cons _________
;     (map
;       (lambda (option) (cons _______________ (cdr option)))
;       (car (cdr (cdr switch-expr))))))
