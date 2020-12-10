
(load-file "../common/common.clj")

(def nums (vec (sort (vec (map to-int input)))))

(def nums (vec (concat (cons 0 nums) (vec (list (+ 3 (apply max nums)))))))

(defn works? [i j]
  (if (or (>= j (count nums)) (>= i (count nums)))
    0
    (if (<= (- (nums j) (nums i)) 3)
      1
      0)))

(defn choices-for [i]
  (max 1 (+ (works? i (+ 1 i)) (works? i (+ 2 i)) (works? i (+ 3 i)))))

(def choices (vec (map choices-for (range (count nums)))))

(def calc-for
  (memoize (fn [i]
             (if (>= i (count choices))
               0
               (case (choices i)
                 1 (calc-for (inc i))
                 2 (+ 1 (calc-for (inc i)) (calc-for (+ 2 i)))
                 3 (+ 2 (calc-for (inc i)) (calc-for (+ 2 i)) (calc-for (+ 3 i))))))))

(inc (calc-for 0))
