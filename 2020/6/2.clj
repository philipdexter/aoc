
(load-file "../common/common.clj")

(def a-z (set (map char (range (int \a) (inc (int \z))))))

(reduce + 0 (map (comp count set) (map #(reduce set/intersection a-z (map set %)) input-split-lines)))
