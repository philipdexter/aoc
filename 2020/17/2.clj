
(load-file "../common/common.clj")

(def state
  (into {} (apply concat (map-indexed (fn [y row]
                                        (map-indexed (fn [x c]
                                                       [[x y 0 0] (= \# c)])
                                                     row)) input))))

(defn neighbor-coords [x y z w]
  [
   [(inc x) (inc y) (inc z) (inc w)]
   [(inc x) (inc y)      z  (inc w)]
   [(inc x) (inc y) (dec z) (inc w)]
   [(inc x)      y  (inc z) (inc w)]
   [(inc x)      y       z  (inc w)]
   [(inc x)      y  (dec z) (inc w)]
   [(inc x) (dec y) (inc z) (inc w)]
   [(inc x) (dec y)      z  (inc w)]
   [(inc x) (dec y) (dec z) (inc w)]
   [     x  (inc y) (inc z) (inc w)]
   [     x  (inc y)      z  (inc w)]
   [     x  (inc y) (dec z) (inc w)]
   [     x       y  (inc z) (inc w)]
   [     x       y       z  (inc w)]
   [     x       y  (dec z) (inc w)]
   [     x  (dec y) (inc z) (inc w)]
   [     x  (dec y)      z  (inc w)]
   [     x  (dec y) (dec z) (inc w)]
   [(dec x) (inc y) (inc z) (inc w)]
   [(dec x) (inc y)      z  (inc w)]
   [(dec x) (inc y) (dec z) (inc w)]
   [(dec x)      y  (inc z) (inc w)]
   [(dec x)      y       z  (inc w)]
   [(dec x)      y  (dec z) (inc w)]
   [(dec x) (dec y) (inc z) (inc w)]
   [(dec x) (dec y)      z  (inc w)]
   [(dec x) (dec y) (dec z) (inc w)]
   [(inc x) (inc y) (inc z)      w]
   [(inc x) (inc y)      z       w]
   [(inc x) (inc y) (dec z)      w]
   [(inc x)      y  (inc z)      w]
   [(inc x)      y       z       w]
   [(inc x)      y  (dec z)      w]
   [(inc x) (dec y) (inc z)      w]
   [(inc x) (dec y)      z       w]
   [(inc x) (dec y) (dec z)      w]
   [     x  (inc y) (inc z)      w]
   [     x  (inc y)      z       w]
   [     x  (inc y) (dec z)      w]
   [     x       y  (inc z)      w]
   ; [     x       y       z       w]
   [     x       y  (dec z)      w]
   [     x  (dec y) (inc z)      w]
   [     x  (dec y)      z       w]
   [     x  (dec y) (dec z)      w]
   [(dec x) (inc y) (inc z)      w]
   [(dec x) (inc y)      z       w]
   [(dec x) (inc y) (dec z)      w]
   [(dec x)      y  (inc z)      w]
   [(dec x)      y       z       w]
   [(dec x)      y  (dec z)      w]
   [(dec x) (dec y) (inc z)      w]
   [(dec x) (dec y)      z       w]
   [(dec x) (dec y) (dec z)      w]
   [(inc x) (inc y) (inc z) (dec w)]
   [(inc x) (inc y)      z  (dec w)]
   [(inc x) (inc y) (dec z) (dec w)]
   [(inc x)      y  (inc z) (dec w)]
   [(inc x)      y       z  (dec w)]
   [(inc x)      y  (dec z) (dec w)]
   [(inc x) (dec y) (inc z) (dec w)]
   [(inc x) (dec y)      z  (dec w)]
   [(inc x) (dec y) (dec z) (dec w)]
   [     x  (inc y) (inc z) (dec w)]
   [     x  (inc y)      z  (dec w)]
   [     x  (inc y) (dec z) (dec w)]
   [     x       y  (inc z) (dec w)]
   [     x       y       z  (dec w)]
   [     x       y  (dec z) (dec w)]
   [     x  (dec y) (inc z) (dec w)]
   [     x  (dec y)      z  (dec w)]
   [     x  (dec y) (dec z) (dec w)]
   [(dec x) (inc y) (inc z) (dec w)]
   [(dec x) (inc y)      z  (dec w)]
   [(dec x) (inc y) (dec z) (dec w)]
   [(dec x)      y  (inc z) (dec w)]
   [(dec x)      y       z  (dec w)]
   [(dec x)      y  (dec z) (dec w)]
   [(dec x) (dec y) (inc z) (dec w)]
   [(dec x) (dec y)      z  (dec w)]
   [(dec x) (dec y) (dec z) (dec w)]
   ])

(defn neighbors [state x y z w]
  (vec (map (fn [[x y z w]] (get state [x y z w])) (neighbor-coords x y z w))))

(defn proc [state x y z w]
  (let [cur (get state [x y z w])
        neighbors (neighbors state x y z w)
        ncount (count (filter identity neighbors))]
    (if cur
      (or (= ncount 2) (= ncount 3))
      (= ncount 3))))

(defn bounds [state]
  (let [xyzws (keys state)
        xs (map first xyzws)
        ys (map second xyzws)
        zs (map #(get % 2) xyzws)
        ws (map #(get % 3) xyzws)
        minx (apply min xs)
        maxx (apply max xs)
        miny (apply min ys)
        maxy (apply max ys)
        minz (apply min zs)
        maxz (apply max zs)
        minw (apply min ws)
        maxw (apply max ws)]
    [(dec minx) (inc maxx) (dec miny) (inc maxy) (dec minz) (inc maxz) (dec minw) (inc maxw)]))

(defn step [state]
  (let [[minx maxx miny maxy minz maxz minw maxw] (bounds state)]
    (into {} (for [x (range minx (inc maxx))
                   y (range miny (inc maxy))
                   z (range minz (inc maxz))
                   w (range minw (inc maxw))]
               [[x y z w] (proc state x y z w)]))))

(loop [state state
       i 0]
  (if (= i 6) (count (filter identity (vals state))) (recur (step state) (inc i))))
