
(defn file-lines [x]
  (with-open [rdr (clojure.java.io/reader x)]
    (vec (line-seq rdr))))

(defn to-int [x] (Integer/parseInt x))
