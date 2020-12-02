(require '[clojure.string :as str])

(def new-memory (vec (repeat 100 0)))

(defn op-add [memory & args]
  (let [args (vec args)]
    (assoc memory (args 2) (+ (memory (args 0)) (memory (args 1))))))

(defn op-mul [memory & args]
  (let [args (vec args)]
    (assoc memory (args 2) (* (memory (args 0)) (memory (args 1))))))

(defn to-int [x] (Integer/parseInt x))

(defn go [pos program]
  (if (>= pos (count program))
    (print "oob\n")
    (let [op (program pos)]
      (cond
        (= op 99) (do (print "done\n") program)
        (= op 1) (go (+ 4 pos) (op-add program (program (+ 1 pos)) (program (+ 2 pos)) (program (+ 3 pos))))
        (= op 2) (go (+ 4 pos) (op-mul program (program (+ 1 pos)) (program (+ 2 pos)) (program (+ 3 pos))))
        :else (print "bad op code\n")))))

(with-open [rdr (clojure.java.io/reader "1.txt")]
  (let [program (map to-int (str/split (first (line-seq rdr)) #","))]
    (print ((go 0 (assoc (assoc (vec program) 2 2) 1 12)) 0))))
