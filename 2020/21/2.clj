
(load-file "../common/common.clj")

(defn parse [line]
  (let [[_ ins algs] (re-find #"([^(]+) ?(.*)" line)]
    [(str/split ins #" ")
     (if (> (count algs) 0)
       (vec (str/split (subs algs 10 (dec (count algs))) #", "))
       [])]))

(def data (into {} (map parse input)))

(def ingredients (distinct (for [[k v] data
                                 ing k]
                             ing)))

(def procd
  (for [[k v] data
        alg v]
    [alg (set k)]))

(defn step [procd]
  (let [next-procd (for [[alg xs] (group-by first procd)]
                     [alg (apply set/intersection (map second xs))])
        to-remove (filter (fn [[k v]] (= (count v) 1)) next-procd)]
    (reduce (fn [next-procd [k' v']] (map (fn [[k v]] [k (if (not= k k') (set/difference v v') v)]) next-procd)) next-procd to-remove)))

(def definites (reduce (fn [procd _] (step procd)) procd (range 100)))

(str/join "," (map (fn [x] (first (into [] (second x)))) (sort-by first definites)))
