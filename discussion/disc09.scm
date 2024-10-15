(define (fit total n)
    (define (inner total n x)
        (cond 
            ((and (= n 0) (= total 0)) #t)
            ((and (= total 0) (not (= n 0))) #f)
            ((and (not (= total 0)) (= n 0)) #f)
            ((> (* x x) total) #f)
            (else (or (inner (- total (* x x)) (- n 1) (+ x 1)) (inner total n (+ x 1))))
        )
    )
    (inner total n 1)
)



(expect (fit 10 2) #t) ; 1*1 + 3*3
(expect (fit 9 1) #t) ; 3*3
(expect (fit 9 2) #f) ;
(expect (fit 9 3) #f) ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
(expect (fit 25 1) #t) ; 5*5
(expect (fit 25 2) #t) ; 3*3 + 4*4



(define (pair-up s)
    (cond
        ((<= (length s) 3) (cons s nil))
        (else (cons (list (car s) (car (cdr s))) (pair-up (cdr (cdr s)))))
    
    )
)


(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )