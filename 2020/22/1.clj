
(load-file "../common/common.clj")

(def player-1 (vec (map to-int (rest (first input-split-lines)))))
(def player-2 (vec (map to-int (rest (second input-split-lines)))))

(defn round [p1 p2]
  (let [x (first p1)
        y (first p2)
        xs (rest p1)
        ys (rest p2)]
    (if (> x y)
      [(concat xs [x y]) ys]
      [xs (concat ys [y x])])))

(defn done [xs]
  (apply + (map #(* %1 %2) xs (reverse (range 1 (inc (count xs)))))))

(loop [p1 player-1
       p2 player-2]
  (let [[p1 p2] (round p1 p2)]
    (cond
      (empty? p1) (done p2)
      (empty? p2) (done p1)
      :else (recur p1 p2))))
