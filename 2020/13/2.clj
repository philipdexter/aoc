
(load-file "../common/common.clj")

(def buses (vec (map (fn [[i x]] [i (to-int x)]) (filter (fn [[i x]] (not= "x" x)) (map-indexed vector (str/split (get input 1) #","))))))

(for [[i bus] buses]
  (println (format "(n+%d)%%%d," i bus)))
