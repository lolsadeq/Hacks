
;; This returns the Nth fibonacci number
(define (fib n)
  (cond ((< n 2) n)
        (else (+ (fib (- n 1)) 
                 (fib (- n 2))))))

;; This will return a list of N fibs 
;; Iterate from 0 to n
;; grab the N fib
;; append to the list
;; return the list at the end of recursion
;; TODO - Make this a flat list instead of nested
(define (fiblist n)
  ;;(print n)
  (cond ((<= n 0) (list 0))
        ((= n 1) (list 0 1))
        (else (list (fiblist (- n 1))
                    (fib n)))))

(define (fiblist2 n)
  (list (fiblist2 (- n 1)) 
        (fib n)))

(define fibonacci
  (λ (n)
    (case n
      ((1 2) 1)
      (else (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))))

(define (fibslow n)
  (cond ((< n 2) n)
        (else (+ (fibslow (- n 1))
                 (fibslow (- n 2))))))

(define (fibfast n)
  (cond ((< n 2) n)
        (else (fibup n 2 1 0))))

(define (fibup max count n-1 n-2)
  (cond ((= max count) (+ n-1 n-2))
        (else (fibup max (+ 1 count) (+ n-1 n-2) n-1))))



