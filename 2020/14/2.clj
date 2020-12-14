
(load-file "../common/common.clj")

(defn parse [line]
  (let [parts (str/split line #" ")]
    (if (= (get parts 0) "mask")
      (get parts 2)
      [(to-int (get (str/split (get parts 0) #"\[|\]") 1)) (to-int (get parts 2))])))

(def program (vec (map parse input)))

(require '[clojure.pprint :refer (cl-format)])
(defn to-binary [x] (cl-format nil "~36,'0',B" x))

(defn float-for [x]
  (if-let [i (str/index-of x "X")]
    (let [a (str (subs x 0 i) "0" (subs x (inc i)))
          b (str (subs x 0 i) "1" (subs x (inc i)))]
      (concat (float-for a) (float-for b)))
    [x]))
(defn join [m x]
  (case [m x]
    [\0 \0] \0
    [\0 \1] \1
    [\1 \0] \1
    [\1 \1] \1
    [\X \0] \X
    [\X \1] \X))
(defn apply-mask [m x]
  (vec (float-for (apply str (map join m (to-binary x))))))


(defn apply-floats [data mask addr val]
  (reduce (fn [data addr] (assoc data addr val)) data (apply-mask mask addr)))

(apply + (vals (get
                 (reduce
                   (fn [[data mask] line]
                     (if (= 2 (count line))
                       [(apply-floats data mask (get line 0) (get line 1)) mask]
                       [data line]))
                   [{} "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
                   program) 0)))
