
(load-file "../common/common.clj")

(def grid
  (vec (map #(vec (map str %)) input)))

(def height (count grid))
(def width (count (get grid 0)))

(defn get* [x y grid] (get (get grid y) x "."))

(defn adjacent-to [x y grid]
  [(get* (inc x) (inc y) grid)
   (get* (inc x) y grid)
   (get* (inc x) (dec y) grid)
   (get* x (inc y) grid)
   (get* x (dec y) grid)
   (get* (dec x) (inc y) grid)
   (get* (dec x) y grid)
   (get* (dec x) (dec y) grid)])

(defn proc-empty [x y grid]
  (if (empty? (filter #(= "#" %) (adjacent-to x y grid)))
    "#"
    "L"))

(defn proc-occupied [x y grid]
  (if (>= (count (filter #(= "#" %) (adjacent-to x y grid))) 4)
    "L"
    "#"))

(defn proc [x y grid]
  (let [seat (get (get grid y) x)]
    (case seat
      "." "."
      "L" (proc-empty x y grid)
      "#" (proc-occupied x y grid))))

(defn step [grid]
  (vec (map (fn [y] (vec (map (fn [x] (proc x y grid)) (range width)))) (range height))))

(loop [prev grid
       steps 0]
  (let [now (step prev)
        steps (inc steps)]
    (if (= prev now)
      (apply + (map (comp count (partial filter #(= "#" %))) now))
      (recur now steps))))
