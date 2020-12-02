(defn calc [x] (let [fuel (- (quot x 3) 2)]
                 (if (< fuel 0) 0 (+ fuel (calc fuel)))))

(def to-int #(Integer/parseInt %))

(with-open [rdr (clojure.java.io/reader "1.txt")]
  (print (reduce + (map (comp calc to-int) (line-seq rdr)))))
