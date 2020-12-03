
(load-file "../common/common.clj")


(def input (file-lines "1.txt"))

(defn parse [lines]
  (vec (for [line lines]
         (vec (map str line)))))

(def trees (parse input))

(defn at [xs x]
  (if (>= x (count xs)) (xs (mod x (count xs))) (xs x)))

(let [stop (count trees)]
  (loop [x 0
         y 0
         agg 0]
    (if (>= y stop)
      agg
      (recur (+ x 3) (+ y 1) (if (= (at (trees y) x) "#") (inc agg) agg)))))
