
(load-file "../common/common.clj")

(def pkeys (vec (map to-int input)))

(defn transform [subject-number loop-size]
  (reduce (fn [n _] (rem (* n subject-number) 20201227)) 1 (range loop-size)))

(defn find-loop-size [subject-number key]
  (loop [i 1
         k 1]
    (let [k (rem (* k subject-number) 20201227)]
      (if (= k key) i (recur (inc i) k)))))

(def card-pkey (get pkeys 0))
(def door-pkey (get pkeys 1))
(def card-loop-size (find-loop-size 7 card-pkey))
(transform door-pkey card-loop-size)
