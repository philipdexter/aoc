
(load-file "../common/common.clj")

(def player-1 (vec (map to-int (rest (first input-split-lines)))))
(def player-2 (vec (map to-int (rest (second input-split-lines)))))

(defn done [xs]
  (apply + (map #(* %1 %2) xs (reverse (range 1 (inc (count xs)))))))

(declare play)

(defn round [p1 p2]
  (let [x (first p1)
        y (first p2)
        xs (rest p1)
        ys (rest p2)
        num-xs (count xs)
        num-ys (count ys)]
    (if (and (>= num-xs x) (>= num-ys y))
      (let [[winner _] (play (vec (take x xs)) (vec (take y ys)))]
        (if (= winner :p1)
          [(concat xs [x y]) ys]
          [xs (concat ys [y x])]))
      (if (> x y)
        [(concat xs [x y]) ys]
        [xs (concat ys [y x])]))))

(defn play [player-1 player-2 ]
  (loop [p1 player-1
         p2 player-2
         configurations #{}]
    (
     if (contains? configurations [p1 p2])
     [:p1 (done p1)]
     (let [configurations (conj configurations [p1 p2])
           [p1 p2] (round p1 p2)]
       (cond
         (empty? p1) [:p2 (done p2)]
         (empty? p2) [:p1 (done p1)]
         :else (recur p1 p2 configurations))))))

(play player-1 player-2)
