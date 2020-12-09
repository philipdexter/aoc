
(load-file "../common/common.clj")

(def input
  (vec (map bigint input)))

(def data
  (let [start 25
        end (count input)]
    (vec (map (fn [i] [(input i) (subvec input (- i 25) i)]) (range start end)))))

(defn can-sum-to [n xs]
  (let [s (set xs)]
    (some identity (map #(contains? (disj s %) (- n %)) xs))))

(loop [i 0]
  (let [[n xs] (data i)]
    (if (can-sum-to n xs)
      (recur (inc i))
      n)))
