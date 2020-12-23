
(load-file "../common/common.clj")

(def input (vec (map (comp to-int str) (first input))))

(def cups input)

(def cups (concat cups (range (inc (apply max cups)) (inc 1000000))))

(def max-cup (apply max cups))
(def min-cup (apply min cups))

(defn get* [xs x]
  (if (> (count xs) x)
    (get xs x)
    (get xs (- x (count xs)))))

(defn insert-at [to-insert i in]
  (let [[before after] (split-at i in)]
    (concat before to-insert after)))

(defn move [cups]
  (let [cur-cup (first cups)
        next-three (take 3 (rest cups))
        the-rest (drop 4 cups)
        destination-index (loop [i (dec cur-cup)]
                            (let [io (.indexOf the-rest i)]
                              (cond
                                (= i cur-cup) 0
                                (> io -1) (inc io)
                                :else (recur (if (< i min-cup)
                                               max-cup
                                               (dec i))))))
        _ (println (let [i1 (.indexOf cups 1)] [(get* cups (+ 1 i1)) (get* cups (+ 2 i1))]))]
    (vec (concat (insert-at next-three destination-index the-rest) [cur-cup]))))

(reduce (fn [cups i] (let [_ (println i)] (move cups))) cups (range 100))
