
(load-file "../common/common.clj")

(def input
  (vec (map bigint input)))

(defn sums-to [i t agg]
  (let [agg (+ agg (input i))]
    (cond
      (= agg t) i
      (> agg t) false
      :else (sums-to (inc i) t agg))))

(def target 400480901N)

(loop [i 0]
  (if-let [end (sums-to i target 0)]
    (let [xs (map input (range i (inc end)))]
      (+ (apply min xs) (apply max xs)))
    (recur (inc i))))
