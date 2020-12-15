
(load-file "../common/common.clj")

(def nums (vec (map to-int (str/split (get input 0) #","))))

(def said (into {} (map-indexed (fn [a b] [b a]) nums)))

(loop [i (count nums)
       prev (last nums)
       said said]
  (if (= i 30000000)
    prev
    (let [] (if (contains? said prev)
       (let [prev-last-spoken (get said prev)
             now (- (dec i) prev-last-spoken)]
         (recur (inc i) now (assoc said prev (dec i))))
       (recur (inc i) 0 (assoc said prev (dec i)))))))
