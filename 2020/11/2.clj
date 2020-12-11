
(load-file "../common/common.clj")

(def grid
  (vec (map #(vec (map str %)) input)))

(def height (count grid))
(def width (count (get grid 0)))

(defn look [x y grid dir-x dir-y]
  (let [x (+ x dir-x)
        y (+ y dir-y)]
    (case (get (get grid y) x)
      "." (look x y grid dir-x dir-y)
      "L" "L"
      "#" "#"
      nil "."
      )))

(defn adjacent-to [x y grid]
  [(look x y grid 1 1)
   (look x y grid 1 0)
   (look x y grid 1 -1)
   (look x y grid 0 1)
   (look x y grid 0 -1)
   (look x y grid -1 1)
   (look x y grid -1 0)
   (look x y grid -1 -1)])

(defn proc-empty [x y grid]
  (if (empty? (filter #(= "#" %) (adjacent-to x y grid)))
    "#"
    "L"))

(defn proc-occupied [x y grid]
  (if (>= (count (filter #(= "#" %) (adjacent-to x y grid))) 5)
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
