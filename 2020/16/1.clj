
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

(defn invalid-numbers [ticket]
  (map (fn [[x valid]] x) (filter (fn [[x valid]] (not valid)) (map (fn [x] [x (number-valid x)]) ticket))))

(apply + (map (fn [ticket] (apply + (invalid-numbers ticket))) nearby-tickets))
