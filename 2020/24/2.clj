
(load-file "../common/common.clj")

(defn to-tile [[x y z] dir]
  (case dir
    "e"  [(inc x) (dec y)      z]
    "se" [     x  (dec y) (inc z)]
    "sw" [(dec x)      y  (inc z)]
    "w"  [(dec x) (inc y)      z]
    "nw" [     x  (inc y) (dec z)]
    "ne" [(inc x)      y  (dec z)]))

(defn parse-dir [line]
  (case (str (first line))
    "e" ["e" (apply str (rest line))]
    "w" ["w" (apply str (rest line))]
    [(apply str (take 2 line)) (apply str (drop 2 line))]))

(defn parse [line]
  (loop [line line
         res []]
    (if (empty? line)
      (reverse res)
      (let [[dir line] (parse-dir line)]
        (recur line (cons dir res))))))

(def to-flip (map parse input))

(defn flip [tiles tile]
  (let [cur (get tiles tile false)]
    (assoc tiles tile (not cur))))

(def tiles (reduce (fn [tiles dirs]
                     (let [dir (reduce (fn [cur dir] (to-tile cur dir)) [0 0 0] dirs)]
                       (flip tiles dir))) {} to-flip))

(defn neighbors-of [tiles [x y z]]
  (map #(get tiles % false) [
                             [(inc x) (dec y)      z]
                             [     x  (dec y) (inc z)]
                             [(dec x)      y  (inc z)]
                             [(dec x) (inc y)      z]
                             [     x  (inc y) (dec z)]
                             [(inc x)      y  (dec z)]
                             ]))

(defn proc [tiles [x y z]]
  (let [neighbors (neighbors-of tiles [x y z])
        num-black (count (filter identity neighbors))]
    (if (get tiles [x y z] false)
      (if (or (= 0 num-black) (> num-black 2)) false true)
      (if (= 2 num-black) true false))))

(defn step [tiles]
  (let [xyzs (keys tiles)
        xs (map first xyzs)
        ys (map second xyzs)
        zs (map #(get % 2) xyzs)
        minx (apply min xs)
        maxx (apply max xs)
        miny (apply min ys)
        maxy (apply max ys)
        minz (apply min zs)
        maxz (apply max zs)]
    (into {} (for [x (range (dec minx) (+ 2 maxx))
                   y (range (dec miny) (+ 2 maxy))
                   z (range (dec minz) (+ 2 maxz))]
               (if (proc tiles [x y z]) [[x y z] true] nil)))))

(defn num-black [tiles]
  (count (filter identity (vals tiles))))

(num-black (reduce (fn [tiles _] (step tiles)) tiles (range 100)))
