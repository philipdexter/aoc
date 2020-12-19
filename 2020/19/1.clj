
(load-file "../common/common.clj")

(def rules (vec (get (vec input-split-lines) 0)))
(def input (vec (get (vec input-split-lines) 1)))

(def rules (into {} (map (fn [line] (str/split line #": ")) rules)))

(defn string-for-rule [n]
  (let [rule (get rules n)]
    (if-let [[_ match] (re-matches #"\"(.*)\"" rule)]
      match
      (let [alts (str/split rule #" \| ")
            alt-strings (map #(map (fn [n] (string-for-rule n)) (str/split % #" ")) alts)]
        (str "(" (str/join "|" (map (partial apply str) (vec (map vec alt-strings)))) ")")))))

(count (filter #(re-matches (re-pattern (string-for-rule "0")) %) input))
