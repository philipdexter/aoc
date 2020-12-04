
(defn file-lines [x]
  (with-open [rdr (clojure.java.io/reader x)]
    (vec (line-seq rdr))))

(defn to-int [x] (Integer/parseInt x))

(def input (file-lines "1.txt"))

(require '[clojure.string :as str])
