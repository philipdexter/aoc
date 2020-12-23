
(load-file "../common/common.clj")

(def input (vec (map (comp to-int str) (first input))))

(def cups input)

(def max-cup (apply max cups))
(def min-cup (apply min cups))

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
                                               (dec i))))))]
    (vec (concat (insert-at next-three destination-index the-rest) [cur-cup]))))

(reduce (fn [cups _] (move cups)) cups (range 100))
