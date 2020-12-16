
(load-file "../common/common.clj")

(def nearby-tickets
  (vec (map #(vec (map to-int (str/split % #","))) input)))

(defn between [a b]
  (fn [x] (and (>= x a) (<= x b))))

(def rules
  [
   (between 27 672)
   (between 680 954)
   (between 25 430)
   (between 439 966)
   (between 31 293)
   (between 299 953)
   (between 29 749)
   (between 775 955)
   (between 43 93)
   (between 107 953)
   (between 50 916)
   (between 941 963)
   (between 31 682)
   (between 702 954)
   (between 38 663)
   (between 672 960)
   (between 31 629)
   (between 635 969)
   (between 42 365)
   (between 371 967)
   (between 30 147)
   (between 167 966)
   (between 39 525)
   (between 545 967)
   (between 30 803)
   (between 822 950)
   (between 39 235)
   (between 257 957)
   (between 33 206)
   (between 231 971)
   (between 29 784)
   (between 798 951)
   (between 38 302)
   (between 316 957)
   (between 50 635)
   (between 642 966)
   (between 25 502)
   (between 510 973)
   (between 42 843)
   (between 861 965)
   ])

(def my-ticket
  [73 53 173 107 113 89 59 167 137 139 71 179 131 181 67 83 109 127 61 79])

(defn number-valid [x]
  (some identity (map #(% x) rules)))

(defn is-valid [ticket]
  (every? identity (map number-valid ticket)))

(def valid-tickets (vec (filter is-valid nearby-tickets)))

(defn ranges [i s a b c d]
  [i s (fn [x] (or (and (>= x a) (<= x b)) (and (>= x c) (<= x d))))])

(def constraints
  [
   (ranges 1 true 27 672 680 954)
   (ranges 2 true 25 430 439 966)
   (ranges 3 true 31 293 299 953)
   (ranges 4 true 29 749 775 955)
   (ranges 5 true 43 93 107 953)
   (ranges 6 true 50 916 941 963)
   (ranges 7 nil 31 682 702 954)
   (ranges 8 nil 38 663 672 960)
   (ranges 9 nil 31 629 635 969)
   (ranges 10 nil 42 365 371 967)
   (ranges 11 nil 30 147 167 966)
   (ranges 12 nil 39 525 545 967)
   (ranges 13 nil 30 803 822 950)
   (ranges 14 nil 39 235 257 957)
   (ranges 15 nil 33 206 231 971)
   (ranges 16 nil 29 784 798 951)
   (ranges 17 nil 38 302 316 957)
   (ranges 18 nil 50 635 642 966)
   (ranges 19 nil 25 502 510 973)
   (ranges 20 nil 42 843 861 965)
   ])

; (def constraints
;   [
;    (ranges true 0  1  4 19)
;    (ranges true 0  5  8 19)
;    (ranges true 0 13 16 19)
;    ])
; (def valid-tickets [
;                     [3,9,18]
;                     [15,1,5]
;                     [5,14,9]
;                     ])

(defn satisfies-range [x range]
  ((get range 2) x))

(def slots
  (vec (map (fn [_] constraints) constraints)))

(def possibilities (vec (map vec (reduce
                                   (fn [slots ticket]
                                     (vec (map (fn [slot n]
                                                 (filter identity (map
                                                                    (fn [range]
                                                                      (if (satisfies-range n range) range nil))
                                                                    slot)))
                                               slots
                                               ticket)))
                                   slots
                                   valid-tickets))))


(defn remove [xs n]
  (vec (filter (partial not= n) xs)))

(defn remove-nth [n xs]
  (let [to-remove (get (get xs n) 0)]
    (vec (map-indexed (fn [i x] (if (= i n) x (remove x to-remove))) xs))))
