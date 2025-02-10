(define (over-or-under num1 num2) 
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1)
  )
)

(define (make-adder num) 
  (lambda (inc) (+ num inc))
)

(define (composed f g) 
  (lambda (x) (f (g x)))
)

(define (repeat f n) 
  (lambda (x) 
    (cond
      ((= n 0) x)
      (else ((repeat f (- n 1)) (f x)))
    )
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (cond
    ((zero? (modulo (max a b) (min a b))) (min a b))
    (else (gcd (min a b) (modulo (max a b) (min a b))))
  )
)
