
(load-file "../common/common.clj")

(defn parse [x]
  (let [[top & contains] (str/split x #", ")]
    (map (fn [x] [top (subs x 2)]) contains)))

(defn proc-one [m x]
  (let [[top contains] x
        existing (get m contains #{})]
    (assoc m contains (conj existing top))))

(defn proc [m xs] (reduce proc-one m xs))

(defn get-set [m x]
  (let [xs (get m x #{})]
    (set/union xs (apply set/union (map (comp set #(get-set m %)) xs)))))

(count (get-set (reduce proc {} (map parse input)) "shiny gold"))
