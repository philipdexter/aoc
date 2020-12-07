
(load-file "../common/common.clj")

(defn parse [x]
  (let [[top & contains] (str/split x #", ")]
    (map (fn [x] [top [(subs x 0 1) (subs x 2)]]) contains)))

(defn proc-one [m x]
  (let [[top [amount contains]] x
        existing (get m top {})]
    (assoc m top (assoc existing contains (+ (to-int amount) (get existing contains 0))))))

(defn proc [m xs] (reduce proc-one m xs))

(defn sum-of [m x]
  (let [xs (get m x {})]
    (reduce + 1 (map (fn [[k v]] (* v (sum-of m k))) xs))))

(dec (sum-of (reduce proc {} (map parse input)) "shiny gold"))
