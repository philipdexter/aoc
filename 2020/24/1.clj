
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

(count (filter identity (vals (reduce (fn [tiles dirs]
                                           (let [dir (reduce (fn [cur dir] (to-tile cur dir)) [0 0 0] dirs)]
                                             (flip tiles dir))) {} to-flip))))
