
(load-file "../common/common.clj")

(def start (to-int (get input 0)))
(def buses (vec (map to-int (filter #(not= "x" %) (str/split (get input 1) #",")))))

(def waits (map #(- (* % (inc (Math/floor (/ start %)))) start) buses))

(let [[i wait] (apply min-key second (map-indexed vector waits))]
  (* wait (get buses i)))
