
(load-file "../common/common.clj")

(defn parse [line]
  (let [parts (str/split line #" ")]
    (if (= (get parts 0) "mask")
      (get parts 2)
      [(to-int (get (str/split (get parts 0) #"\[|\]") 1)) (to-int (get parts 2))])))

(def program (vec (map parse input)))

(require '[clojure.pprint :refer (cl-format)])
(defn to-binary [x] (cl-format nil "~36,'0',B" x))

(defn join [m x]
  (case [m x]
    [\0 \0] \0
    [\0 \1] \0
    [\1 \0] \1
    [\1 \1] \1
    [\X \0] \0
    [\X \1] \1))
(defn apply-mask [m x] (Long/parseLong (apply str (map join m (to-binary x))) 2))


(apply + (vals (get
                 (reduce
                   (fn [[data mask] line]
                     (if (= 2 (count line))
                       [(assoc data (get line 0) (apply-mask mask (get line 1))) mask]
                       [data line]))
                   [{} "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
                   program) 0)))
