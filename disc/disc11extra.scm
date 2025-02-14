(define (up n)
    (define (helper n result)
        (if (zero? n) result
            (helper 
                (quotient n 10) 
                (let ((first (remainder n 10)))
                    (if (< first (car result)) (cons first result)
                        (cons first (cons result nil))
                    )
                )
            )
        
        )
    
    )
    (helper (quotient n 10)
        (cons (remainder n 10) nil)

    )
)

