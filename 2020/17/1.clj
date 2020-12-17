
(load-file "../common/common.clj")

(def state
  (into {} (apply concat (map-indexed (fn [y row]
                                        (map-indexed (fn [x c]
                                                       [[x y 0] (= \# c)])
                                                     row)) input))))

(defn neighbor-coords [x y z]
  [
   [(inc x) (inc y) (inc z)]
   [(inc x) (inc y)      z ]
   [(inc x) (inc y) (dec z)]
   [(inc x)      y  (inc z)]
   [(inc x)      y       z ]
   [(inc x)      y  (dec z)]
   [(inc x) (dec y) (inc z)]
   [(inc x) (dec y)      z ]
   [(inc x) (dec y) (dec z)]
   [     x  (inc y) (inc z)]
   [     x  (inc y)      z ]
   [     x  (inc y) (dec z)]
   [     x       y  (inc z)]
   ; [     x       y       z ]
   [     x       y  (dec z)]
   [     x  (dec y) (inc z)]
   [     x  (dec y)      z ]
   [     x  (dec y) (dec z)]
   [(dec x) (inc y) (inc z)]
   [(dec x) (inc y)      z ]
   [(dec x) (inc y) (dec z)]
   [(dec x)      y  (inc z)]
   [(dec x)      y       z ]
   [(dec x)      y  (dec z)]
   [(dec x) (dec y) (inc z)]
   [(dec x) (dec y)      z ]
   [(dec x) (dec y) (dec z)]
   ])

(defn neighbors [state x y z]
  (vec (map (fn [[x y z]] (get state [x y z])) (neighbor-coords x y z))))

(defn proc [state x y z]
  (let [cur (get state [x y z])
        neighbors (neighbors state x y z)
        ncount (count (filter identity neighbors))]
    (if cur
      (or (= ncount 2) (= ncount 3))
      (= ncount 3))))

(defn bounds [state]
  (let [xyzs (keys state)
        xs (map first xyzs)
        ys (map second xyzs)
        zs (map #(get % 2) xyzs)
        minx (apply min xs)
        maxx (apply max xs)
        miny (apply min ys)
        maxy (apply max ys)
        minz (apply min zs)
        maxz (apply max zs)]
    [(dec minx) (inc maxx) (dec miny) (inc maxy) (dec minz) (inc maxz)]))

(defn step [state]
  (let [[minx maxx miny maxy minz maxz] (bounds state)]
    (into {} (for [x (range minx (inc maxx))
                   y (range miny (inc maxy))
                   z (range minz (inc maxz))]
               [[x y z] (proc state x y z)]))))

(loop [state state
       i 0]
  (if (= i 6) (count (filter identity (vals state))) (recur (step state) (inc i))))
