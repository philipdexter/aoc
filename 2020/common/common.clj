
(defn file-lines [x]
  (with-open [rdr (clojure.java.io/reader x)]
    (vec (line-seq rdr))))

(defn to-int [x] (Integer/parseInt x))

(defn abs [x] (if (< 0 x) x (- x)))

(def input (file-lines "1.txt"))

(require '[clojure.string :as str])
(require '[clojure.set :as set])


(def input-split-lines
  (loop [agg '()
         tail input]
    (let [[took dropped] (split-with not-empty tail)]
      (if (not-empty dropped)
        (recur (concat agg [took]) (rest dropped))
        (concat agg [took])))))
