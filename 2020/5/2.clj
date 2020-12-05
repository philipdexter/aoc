
(load-file "../common/common.clj")

(defn floor [x] (int (Math/floor x)))
(defn ceil [x] (int (Math/ceil x)))

(defn F [cur]
  [(cur 0) (floor (+ (cur 0) (/ (- (cur 1) (cur 0)) 2)))])
(defn B [cur]
  [(ceil (+ (cur 0) (/ (- (cur 1) (cur 0)) 2))) (cur 1)])

(defn row-dir-to-f [x]
  (if (= x "F") F B))

(defn do-row [dirs]
  ((reduce
     (fn [state dir] ((row-dir-to-f dir) state))
     [0 127]
     (map str dirs)) 0))

(defn col-dir-to-f [x]
  (if (= x "L") F B))

(defn do-col [dirs]
  ((reduce
     (fn [state dir] ((col-dir-to-f dir) state))
     [0 7]
     (map str dirs)) 0))

(defn parse [x]
  (let [row-dirs (subs x 0 7)
        col-dirs (subs x 7)]
    [(do-row row-dirs) (do-col col-dirs)]))

(require '[clojure.set :as set])

(set/difference
  (set (range 12 859))
  (sort (map (comp #(+ (* 8 (% 0)) (% 1)) parse) input)))
