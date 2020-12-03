
(load-file "../common/common.clj")


(def input (file-lines "1.txt"))

(defn parse [lines]
  (vec (for [line lines]
         (vec (map str line)))))

(def trees (parse input))

(defn at [xs x]
  (if (>= x (count xs)) (xs (mod x (count xs))) (xs x)))

(defn answer-for [right down]
  (let [stop (count trees)]
    (loop [x 0
           y 0
           agg 0]
      (if (>= y stop)
        agg
        (recur (+ x right) (+ y down) (if (= (at (trees y) x) "#") (inc agg) agg))))))

(*
 (answer-for 1 1)
 (answer-for 3 1)
 (answer-for 5 1)
 (answer-for 7 1)
 (answer-for 1 2))
